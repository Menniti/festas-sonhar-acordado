# -*- coding: utf-8 -*-
import re
from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.models import ST_PP_COMPLETED
from subscriptions.models import Subscription, SubscriptionPayment


def detect_payment_and_mark_subscription(sender, **kwargs):
    if sender.payment_status != ST_PP_COMPLETED:
        return

    match = re.search('^Subscription\(id=(\d+)\)$', sender.invoice)
    if match:
        pk = int(match.group(1))
        Subscription.objects.filter(pk=pk)\
                            .update(paid=sender.payment_gross,
                                    payment='eletronic')
        SubscriptionPayment.objects\
                           .create(subscription_id=pk,
                                   content_object=sender)

valid_ipn_received.connect(detect_payment_and_mark_subscription)
