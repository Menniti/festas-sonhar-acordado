# -*- coding: utf-8 -*-
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from communication.models import ScheduledEmail
from trainings.models import Training
from dynamic_preferences import global_preferences_registry


preferences = global_preferences_registry.manager()
offset_days = preferences['training__notification_before']
target_date = now() + timedelta(offset_days)


class Command(BaseCommand):
    help = 'Envia lembrete de treinamento para o voluntários'
    queryset = ScheduledEmail.objects\
        .select_related('template')\
        .filter(
            training__date__gt=now(),
            training__date__lt=target_date
        )

    def send_scheduled_emails(self, schedule, recipients):
        tpl = schedule.template
        msg = EmailMultiAlternatives(tpl.subject, tpl.text_content, tpl.sender, recipients)
        msg.attach_alternative(tpl.html_content, "text/html")
        msg.send()

    def handle(self, *args, **options):
        for schedule in self.queryset:
            training = schedule.content_object
            recipients = (
                '{name} <{email}>'.format(name=name, email=email)
                for name, email in training.subscription_set
                                           .values_list('volunteer__name',
                                                        'volunteer__email')
            )

            self.send_scheduled_emails(schedule, recipients)

        #self.queryset.update(sent=now())
