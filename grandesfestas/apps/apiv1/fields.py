# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.utils import timezone


class DateTimeTzAwareField(serializers.DateTimeField):
    """ Return datetime for a field in serializer
    based on settings.TIME_ZONE instead UTC """

    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeTzAwareField, self).to_representation(value)
