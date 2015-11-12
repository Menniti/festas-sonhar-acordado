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
    date = DateTimeTzAwareField(format="%d/%m/%Y, %H:%M")

    class Meta:
        model = Training
        fields = ('id', 'local', 'date')


class VolunteerSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of volunteers.models.Volunteer """
    birthdate = serializers.DateField(input_formats=["%d/%m/%Y"])

    class Meta:
        model = Volunteer
        fields = ('id', 'email', 'name', 'rg', 'birthdate', 'phone', 'occupation',
                  'organization', 'cep', 'address', 'complement', 'state', 'city',)

    @property
    def data(self):
        ret = super(self.__class__, self).data
        request = self.context.get('request')

        if request.data and not request.user.is_authenticated():
            keys = list(ret.keys())
            for key in keys:
                if key != 'id' and key not in request.data:
                    ret.pop(key)
        return ret


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of subscriptions.models.Subscription """
    special = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ('id', 'volunteer', 'training', 'present', 'paid',
                  'payment', 'extra', 'valid', 'special')

    @property
    def data(self):
        ret = super(self.__class__, self).data
        request = self.context.get('request')

        if request.data and not request.user.is_authenticated():
            public = {'id', 'special'}
            keys = list(ret.keys())
            for key in keys:
                if key not in public and key not in request.data:
                    ret.pop(key)
        return ret

    def get_special(self, obj):
        return obj.volunteer.project != ''

    def validate(self, validated_data):
        stub = {'user': {'is_authenticated': lambda: False}}
        if not self.context.get('request', stub).user.is_authenticated():
            validated_data.pop('paid', None)
            validated_data.pop('present', None)
            validated_data.pop('valid', None)
        return super(SubscriptionSerializer, self).validate(validated_data)


class ContactEmailSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of communication.models.ContactEmail """

    class Meta:
        model = ContactEmail
        fields = ('email', 'name', 'subject', 'content',)
