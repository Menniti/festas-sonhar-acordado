# -*- coding: utf-8 -*-
from urllib.parse import urljoin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from rest_framework import filters, viewsets
from rest_framework.decorators import detail_route, list_route
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

from bcash.forms import BcashForm


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.select_related('local')\
                               .filter(date__gte=now())\
                               .order_by('date')
    serializer_class = TrainingSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('volunteer',)
    permission_classes = (AuthOrWriteOnly,)
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def create(self, request):
        volunteer = request.data.get('volunteer')
        instance = self.queryset.filter(volunteer=volunteer).first()
        if instance and instance.id:
            self.kwargs.update({'pk': instance.id})
            return super(self.__class__, self).update(request, **self.kwargs)
        return super(self.__class__, self).create(request)


class VolunteerViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('email',)
    permission_classes = [AuthOrWriteOnly, ]
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

    def create(self, request):
        email = request.data.get('email')
        instance = self.queryset.filter(email=email).first()
        if instance and instance.id:
            self.kwargs.update({'pk': instance.id})
            return super(self.__class__, self).update(request, **self.kwargs)
        return super(self.__class__, self).create(request)


class PaypalFormAPIView(APIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def get(self, request, subscription_id):
        preferences = global_preferences_registry.manager()
        subscription = get_object_or_404(Subscription, id=int(subscription_id))
        volunteer = subscription.volunteer

        form = PayPalPaymentsForm(initial={
            'business':         preferences['payment__receiver_email'],
            'amount':           preferences['subscription__ticket_value'],
            'custom':           preferences['payment__campaign'],
            'item_name':        preferences['payment__item_name'].format(volunteer.name),
            'item_number':      subscription_id,
            'notify_url':       urljoin(preferences['general__site_url'], reverse('paypal-ipn')),
            'invoice':          'Subscription(id=%s)' % subscription_id,
            'currency_code':    'BRL',
            'lc':               'BR',
            'no_shipping':      '1',
            'address_override': '1',
            'country':          'BR',

            'first_name':      volunteer.first_name(),
            'last_name':       volunteer.last_name(),
            'address1':        volunteer.address,
            'address2':        volunteer.complement,
            'city':            volunteer.city,
            'state':           volunteer.state,
            'zip':             volunteer.cep,
            'night_phone_a':   '',
            'night_phone_b':   '',
            'night_phone_c':   '',
            'email':           volunteer.email,
        })

        data = dict([(f.name, f.value()) for f in form if f.value() is not None])
        data['endpoint'] = form.get_endpoint()
        data['image_button'] = form.get_image()

        response = Response(data)
        return response


class BcashFormAPIView(APIView):
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    def get(self, request, subscription_id):
        preferences = global_preferences_registry.manager()
        subscription = get_object_or_404(Subscription, id=int(subscription_id))
        volunteer = subscription.volunteer
        secret = preferences['payment__bcash_secret']

        form = BcashForm(secret=secret, initial={
            'campanha':            preferences['payment__campaign'],
            'cod_loja':            preferences['payment__bcash_cod_loja'],
            'email_loja':          preferences['payment__receiver_email'],
            'meio_pagamento':      10,
            'parcela_maxima':      1,
            'produto_codigo_1':    subscription_id,
            'produto_descricao_1': preferences['payment__item_name'].format(volunteer.name),
            'produto_qtde_1':      1,
            'produto_valor_1':     preferences['subscription__ticket_value'],
            'redirect':            'true',
            'redirect_time':       '10',
            'url_retorno':         urljoin(preferences['general__site_url'], reverse('bcash:return_url')),
        })

        data = {
            'fields': form.to_json()
        }
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
