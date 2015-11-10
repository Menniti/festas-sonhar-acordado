# -*- coding: utf-8 -*-
import re
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.models import ST_PP_COMPLETED
from bcash.models import Transaction, ST_APPROVED
from subscriptions.models import Subscription, SubscriptionPayment


def detect_paypal_payment_and_mark_subscription(sender, **kwargs):
    match = re.search('^Subscription\(id=(\d+)\)$', sender.invoice)

    if match:
        pk = int(match.group(1))
        qs = Subscription.objects.filter(pk=pk)

        if qs.exists():
            if sender.payment_status == ST_PP_COMPLETED:
                qs.update(paid=sender.payment_gross, payment='eletronic')

            SubscriptionPayment.objects.create(
                subscription_id=pk,
                content_object=sender
            )
valid_ipn_received.connect(detect_paypal_payment_and_mark_subscription)


@receiver(post_save, sender=Transaction)
def detect_bcash_payment_and_mark_subscription(sender, instance, **kwargs):
    data = getattr(instance, 'json_data', {})
    pk = int(data.get('produto_codigo_1', 0))
    val = float(data.get('produto_valor_1', 0))
    qs = Subscription.objects.filter(pk=pk)

    if qs.exists():
        if instance.status_code == ST_APPROVED:
            qs.update(paid=val, payment='eletronic')

        content_type = ContentType.objects.get_for_model(instance)

        SubscriptionPayment.objects.get_or_create(
            subscription_id=pk,
            content_type=content_type,
            object_id=instance.id
        )
