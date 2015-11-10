# -*- coding: utf-8 -*-
from django import forms
from collections import OrderedDict
from hashlib import md5
from unicodedata import normalize

try:
    from urllib.parse import urlencode
except ImportError as e:
    from urllib import urlencode

BCASH_ENDPOINT = 'https://www.bcash.com.br/checkout/pay/'
IMAGE_BUTTON_90 = 'https://a248.e.akamai.net/f/248/96284/168h/www.bcash.com.br/webroot/banners/site/bc90x95px.png'


def remove_diacritic(word):
    return normalize('NFKD', word)\
        .encode('ASCII', 'ignore')\
        .decode('ASCII')


class BcashForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.secret = kwargs.pop('secret', None)
        super(BcashForm, self).__init__(*args, **kwargs)

    campanha = forms.CharField(widget=forms.HiddenInput)
    cod_loja = forms.CharField(widget=forms.HiddenInput)
    email_loja = forms.CharField(widget=forms.HiddenInput)
    meio_pagamento = forms.CharField(widget=forms.HiddenInput, initial='10')
    parcela_maxima = forms.CharField(widget=forms.HiddenInput, initial='1')
    produto_codigo_1 = forms.CharField(widget=forms.HiddenInput)
    produto_descricao_1 = forms.CharField(widget=forms.HiddenInput)
    produto_qtde_1 = forms.CharField(widget=forms.HiddenInput)
    produto_valor_1 = forms.CharField(widget=forms.HiddenInput)
    #redirect = forms.CharField(widget=forms.HiddenInput)
    #redirect_time = forms.CharField(widget=forms.HiddenInput, initial='10')

    def to_json(self):
        items = []

        for key in sorted(self.fields.keys()):
            f = self[key]
            n = str(f.name)
            if type(f.value()) is str:
                v = remove_diacritic(f.value())
            elif type(f.value()) is float:
                v = "%.2f" % f.value()
            else:
                v = str(f.value())
            items.append((n, v,))

        data = OrderedDict(items)

        if self.secret:
            url = (urlencode(data) + self.secret).encode('utf-8')
            data['hash'] = md5(url).hexdigest()

        return data

    def get_image(self):
        return IMAGE_BUTTON_90

    def get_endpoint(self):
        return BCASH_ENDPOINT
