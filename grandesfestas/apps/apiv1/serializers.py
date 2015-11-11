# -*- coding: utf-8 -*-
from rest_framework import serializers
from apiv1.fields import DateTimeTzAwareField

from communication.models import ContactEmail
from trainings.models import Training, TrainingLocal
from volunteers.models import Volunteer
from subscriptions.models import Subscription


class TrainingLocalSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of trainings.models.TrainingLocal """

    class Meta:
        model = TrainingLocal
        fields = ('id', 'name', 'cep', 'address', 'complement',
                  'state', 'city', 'lat', 'lon',)


class TrainingSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of trainings.models.Training """
    local = TrainingLocalSerializer(read_only=True)
    date = DateTimeTzAwareField()

    class Meta:
        model = Training
        fields = ('id', 'local', 'date')


class VolunteerSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of volunteers.models.Volunteer """

    class Meta:
        model = Volunteer
        fields = ('id', 'email', 'name', 'rg', 'birthdate', 'phone', 'occupation',
                  'organization', 'cep', 'address', 'complement', 'state', 'city',)

    @property
    def data(self):
        ret = super(self.__class__, self).data
        request = self.context.get('request')
        if request.data and not request.user.is_authenticated():
            new_ret = dict([(k, ret.get(k)) for k in request.data.keys() if k in ret])
            if 'id' in ret:
                new_ret['id'] = ret.get('id')
            return new_ret
        return ret


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of subscriptions.models.Subscription """

    class Meta:
        model = Subscription
        fields = ('id', 'volunteer', 'training', 'present', 'paid',
                  'payment', 'extra', 'valid',)

    @property
    def data(self):
        ret = super(self.__class__, self).data
        request = self.context.get('request')
        if request.data and not request.user.is_authenticated():
            new_ret = dict([(k, ret.get(k)) for k in request.data.keys() if k in ret])
            if 'id' in ret:
                new_ret['id'] = ret.get('id')
            return new_ret
        return ret


class ContactEmailSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of communication.models.ContactEmail """

    class Meta:
        model = ContactEmail
        fields = ('email', 'name', 'subject', 'content',)
