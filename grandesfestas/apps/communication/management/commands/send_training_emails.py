# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template import engines
from django.utils.timezone import now, timedelta

from communication.models import ScheduledEmail
from trainings.models import Training
from dynamic_preferences import global_preferences_registry

django_engine = engines['django']

preferences = global_preferences_registry.manager()
offset_days = preferences['training__notification_before']
target_date = now() + timedelta(offset_days)


class Command(BaseCommand):
    help = 'Envia lembrete de treinamento para o voluntários'
    queryset = ScheduledEmail.objects\
        .select_related('template')\
        .filter(
            training__date__gt=now(),
            training__date__lt=target_date,
            sent=None
        )

    def send_scheduled_emails(self, schedule, training, recipients):
        base = schedule.template

        html_content = django_engine.from_string(base.html_content).render({'training': training})
        text_content = django_engine.from_string(base.text_content).render({'training': training})

        msg = EmailMultiAlternatives(base.subject, text_content, base.sender, recipients)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def handle(self, *args, **options):
        for schedule in self.queryset:
            training = schedule.content_object
            recipients = (
                '{name} <{email}>'.format(name=name, email=email)
                for name, email in training.subscription_set.values_list('volunteer__name', 'volunteer__email')
            )
            self.send_scheduled_emails(schedule, training, recipients)
        self.queryset.update(sent=now())
