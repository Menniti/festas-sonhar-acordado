# -*- coding: utf-8 -*-
from urllib.parse import urljoin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from rest_framework import filters, viewsets
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.views import APIView, Response

from paypal.standard.forms import PayPalPaymentsForm
from dynamic_preferences import global_preferences_registry

from trainings.models import Training
from volunteers.models import Volunteer
from subscriptions.models import Subscription
from communication.models import ContactEmail
from apiv1.serializers import (ContactEmailSerializer,
                               SubscriptionSerializer,
                               TrainingSerializer,
                               VolunteerSerializer, )

from apiv1.renderers import JSONRenderer
from apiv1.permissions import AuthOrWriteOnly


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.select_related('local').all().order_by('date')
    serializer_class = TrainingSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('volunteer',)
    permission_classes = (AuthOrWriteOnly,)
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('email',)
    permission_classes = [AuthOrWriteOnly, ]
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


class PaymentFormAPIView(APIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def get(self, request, subscription_id):
        preferences = global_preferences_registry.manager()
        subscription = get_object_or_404(Subscription, id=int(subscription_id))
        volunteer = subscription.volunteer

        form = PayPalPaymentsForm(initial={
            'amount':           preferences['subscription__ticket_value'],
            'business':         preferences['payment__paypal_receiver_email'],
            'cancel_return':    preferences['payment__cancel_explanation_path'],
            'return':           preferences['payment__return_after_payment'],
            'custom':           preferences['payment__campaign'],
            'item_name':        preferences['payment__item_name'].format(volunteer.name),
            'notify_url':       urljoin(preferences['general__site_url'], reverse('paypal-ipn')),
            'invoice':          'Subscription(id=%s)' % subscription_id,
            'charset':          'utf-8',
            'currency_code':    'BRL',
            'lc':               'BR',
            'no_shipping':      '1',
        })

        data = dict([(f.name, f.value()) for f in form if f.value() is not None])
        data['endpoint'] = form.get_endpoint()
        data['image_button'] = form.get_image()

        response = Response(data)
        return response


class ContactEmailViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('email',)
    permission_classes = [AuthOrWriteOnly, ]
    queryset = ContactEmail.objects.all()
    serializer_class = ContactEmailSerializer
