# -*- coding: utf-8 -*-
import re
import io
import qrcode

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from dynamic_preferences import global_preferences_registry
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.models import ST_PP_COMPLETED
from bcash.models import Transaction, ST_APPROVED
from subscriptions.models import Subscription, SubscriptionPayment

preferences = global_preferences_registry.manager()


def detect_paypal_payment_and_mark_subscription(sender, **kwargs):
    match = re.search('^Subscription\(id=(\d+)\)$', sender.invoice)

    if match:
        pk = int(match.group(1))
        subscription = Subscription.objects.filter(pk=pk).first()

        if subscription:
            if sender.payment_status == ST_PP_COMPLETED:
                subscription.paid = sender.payment_gross
                subscription.payment = 'eletronic'
                subscription.save()

            SubscriptionPayment.objects.create(
                subscription=subscription,
                content_object=sender
            )
valid_ipn_received.connect(detect_paypal_payment_and_mark_subscription)


@receiver(post_save, sender=Transaction)
def detect_bcash_payment_and_mark_subscription(sender, instance, **kwargs):
    data = getattr(instance, 'json_data', {})
    pk = int(data.get('produto_codigo_1', 0))
    val = float(data.get('produto_valor_1', 0))
    subscription = Subscription.objects.filter(pk=pk).first()

    if subscription:
        if instance.status_code == ST_APPROVED:
            subscription.paid = val
            subscription.payment = 'eletronic'
            subscription.save()

        content_type = ContentType.objects.get_for_model(instance)

        SubscriptionPayment.objects.get_or_create(
            subscription=subscription,
            content_type=content_type,
            object_id=instance.id
        )


@receiver(pre_save, sender=Subscription)
def mark_is_subscription_is_valid(sender, instance, **kwargs):
    ticket_value = preferences['subscription__ticket_value']

    if instance.paid >= ticket_value and instance.present:
        instance.valid = True


@receiver(post_save, sender=Subscription)
def draw_qrcode_for_subscription(sender, instance, **kwargs):
    if not instance.image:
        name = 'qrcode%04d-%s.png' % (instance.id, slugify(instance.volunteer.name))
        code = qrcode.make(str(instance.id))
        buf = io.BytesIO()
        code.save(buf)
        buf.size = buf.tell()
        instance.image.save(name, buf)
