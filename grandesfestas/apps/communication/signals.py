# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.template import engines
from django.utils.timezone import timedelta

from dynamic_preferences import global_preferences_registry

from communication.models import ContactEmail, ScheduledEmail, TemplateEmail
from trainings.models import Training
from subscriptions.models import Subscription

django_engine = engines['django']
preferences = global_preferences_registry.manager()


@receiver(post_save, sender=ContactEmail)
def forward_messages_from_contact_to_email(sender, **kwargs):
    if kwargs.get('created', False):
        contact = kwargs.get('instance')
        sender = '{name}<{email}>'.format(name=contact.name, email=contact.email)

        msg = EmailMultiAlternatives(
            contact.subject,
            contact.content,
            sender,
            [settings.DEFAULT_TO_EMAIL],
            headers={'Reply-To': sender}
        )
        msg.send()


@receiver(post_save, sender=Training)
def schedule_email_to_new_training(sender, instance, **kwargs):
    if not kwargs.get('created', False):
        return

    offset_days = preferences['training__notification_before']
    content_type = ContentType.objects.get_for_model(sender)
    template, new = TemplateEmail.objects.get_or_create(content_type=content_type)

    schedule = ScheduledEmail()
    schedule.date = instance.date - timedelta(offset_days)
    schedule.template = template
    schedule.content_object = instance
    schedule.save()


@receiver(post_save, sender=Subscription)
def send_email_in_new_subscription(sender, instance, **kwargs):
    if not kwargs.get('created', False):
        return

    content_type = ContentType.objects.get_for_model(sender)
    template, new = TemplateEmail.objects.get_or_create(content_type=content_type)

    contact = kwargs.get('instance')

    html_content = django_engine.from_string(template.html_content).render({'subscription': instance})
    text_content = django_engine.from_string(template.text_content).render({'subscription': instance})

    msg = EmailMultiAlternatives(
        template.subject,
        text_content,
        template.sender,
        [instance.volunteer.email],
        headers={'Reply-To': template.sender}
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()
