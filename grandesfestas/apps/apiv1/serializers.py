# -*- coding: utf-8 -*-
from rest_framework import serializers
from apiv1.fields import DateTimeTzAwareField

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
        has_id = ret.get('id', False)
        request = self.context.get('request')
        if request and has_id and not request.user.is_authenticated():
            return {'id': ret.get('id')}
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
        has_id = ret.get('id', False)
        request = self.context.get('request')
        if request and has_id and not request.user.is_authenticated():
            return {'id': ret.get('id')}
        return ret
