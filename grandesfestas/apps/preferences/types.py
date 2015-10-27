# -*- coding: utf-8 -*-
from django import forms
from dynamic_preferences.serializers import BaseSerializer
from dynamic_preferences.types import BasePreferenceType


class FloatSerializer(BaseSerializer):
    @classmethod
    def clean_to_db_value(cls, value):
        if type(value) not in (int, float,):
            raise cls.exception('FloatSerializer can only serialize float values')
        return value

    @classmethod
    def to_python(cls, value, **kwargs):
        try:
            return float(value)
        except:
            raise cls.exception("Value {0} cannot be converted to float")


class FloatPreference(BasePreferenceType):
    field_class = forms.FloatField
    serializer = FloatSerializer
