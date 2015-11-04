# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Volunteer(models.Model):
    PROJECTS = (
        ('aps1', _("Amigos para Sempre 1")),
        ('aps2', _("Amigos para Sempre 2")),
        ('aps3', _("Amigos para Sempre 3")),
        ('aps4', _("Amigos para Sempre 4")),
        ('aps5', _("Amigos para Sempre 5")),
        ('sj', _("Sonhando Juntos")),
        ('ppf', _("Preparando para o Futuro")),
    )

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

    project = models.CharField(_('Project'), choices=PROJECTS, max_length=16, blank=True)

    def __str__(self):
        return self.name

    def first_name(self):
        return self.name.split(' ')[0]

    def last_name(self):
        parts = self.name.split(' ')
        return ' '.join(parts[1:]) if len(parts) > 1 else ''

    class Meta:
        verbose_name = _('Volunteer')
        verbose_name_plural = _('Volunteers')
