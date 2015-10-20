# -*- coding: utf-8 -*-
from rest_framework import serializers
from trainings.models import Training, TrainingLocal
from django.utils import timezone


# TODO: move to a file named fields.py
class DateTimeTzAwareField(serializers.DateTimeField):
    """ Return datetime based on settings.TIME_ZONE instead UTC """

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_representation(value)


class TrainingLocalSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of trainings.models.TrainingLocal """

    class Meta:
        model = TrainingLocal
        fields = ('name', 'cep', 'address', 'complement', 'state', 'city', 'lat', 'lon',)


class TrainingSerializer(serializers.ModelSerializer):
    """ Outputs JSON representation of trainings.models.Training """
    local = TrainingLocalSerializer(read_only=True)
    date = DateTimeTzAwareField()

    class Meta:
        model = Training
        fields = ('local', 'date')
