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


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of subscriptions.models.Subscription """
    volunteer = VolunteerSerializer()

    class Meta:
        model = Subscription
        fields = ('id', 'volunteer', 'training', 'present', 'paid',
                  'payment', 'extra', 'valid',)

    def __init__(self, *args, **kwargs):
        """ Constructs SubscriptionSerializer and set existing
         volunteer instance in VolunteerSerializer """
        super(SubscriptionSerializer, self).__init__(*args, **kwargs)
        self.fields['volunteer'].instance = getattr(self.instance, 'volunteer', None)

    def validate(self, validated_data):
        """ Validate content and permission for fields, and
        fails silently for fields 'paid', 'present' and 'valid' """

        stub = {'user': {'is_staff': False}}
        if not self.context.get('request', stub).user.is_staff:
            validated_data.pop('paid', None)
            validated_data.pop('present', None)
            validated_data.pop('valid', None)

        return super(SubscriptionSerializer, self).validate(validated_data)

    def update(self, instance, validated_data):
        """ Update info from Subscription and Volunteer together """
        data = validated_data.pop('volunteer')
        serializer = VolunteerSerializer(instance=instance.volunteer, data=data)

        if serializer.is_valid():
            instance = serializer.save()
            validated_data['volunteer'] = instance

        return super(SubscriptionSerializer, self).update(instance, validated_data)

    def create(self, validated_data):
        """ Create a Volunteer and a Subscription together """
        data = validated_data.pop('volunteer')
        serializer = VolunteerSerializer(data=data)

        if serializer.is_valid():
            instance = serializer.save()
            validated_data['volunteer'] = instance

        return super(SubscriptionSerializer, self).create(validated_data)

    @property
    def data(self):
        """ TODO: workaround! rest_framework is not serializing correctly
        the Foreign to Training models. Bug?? """
        data = super(SubscriptionSerializer, self).data

        if type(data.get('training', None)) is Training:
            data['training'] = data['training'].id

        return data
