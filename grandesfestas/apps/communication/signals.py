# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.conf import settings
from communication.models import ContactEmail


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
