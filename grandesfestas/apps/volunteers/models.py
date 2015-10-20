# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Volunteer(models.Model):
    created_date = models.DateTimeField(_('Created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True, editable=False)

    # identification
    email = models.EmailField(_('Email'), unique=True)
    name = models.CharField(_('Name'), max_length=64)
    rg = models.CharField(_('Rg'), max_length=16)
    birthdate = models.DateField(_('Birthdate'))
    phone = models.CharField(_('Phone'), max_length=32)

    # about
    occupation = models.CharField(_('Occupation'), max_length=32)
    organization = models.CharField(_('Organization'), max_length=32)

    # address
    cep = models.CharField(_('Cep'), max_length=9)
    address = models.CharField(_('Address'), max_length=128)
    complement = models.CharField(_('Complement'), max_length=32, blank=True)
    state = models.CharField(_('State'), max_length=32)
    city = models.CharField(_('City'), max_length=32)

    class Meta:
        verbose_name = _('Volunteer')
        verbose_name_plural = _('Volunteers')
