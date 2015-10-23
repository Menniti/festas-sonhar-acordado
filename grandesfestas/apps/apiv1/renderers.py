# -*- coding: utf-8 -*-
from rest_framework import renderers
from rest_framework.utils import encoders


class JSONEncoder(encoders.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_json'):
            return o.to_json()
        raise super(encoders.JSONEncoder, self).default(o)


class JSONRenderer(renderers.JSONRenderer):
    encoder_class = JSONEncoder
