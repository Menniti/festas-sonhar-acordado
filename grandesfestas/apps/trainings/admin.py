# -*- coding: utf-8 -*-
from django.contrib import admin
from trainings.models import Training, TrainingLocal
from django.utils.translation import ugettext_lazy as _
from dynamic_preferences import global_preferences_registry
from django.utils import numberformat

preferences = global_preferences_registry.manager()


def format_money(value):
    return numberformat.format(
        value,
        decimal_pos=2,
        decimal_sep=',',
        force_grouping=True,
        grouping=3,
        thousand_sep='.'
    )


@admin.register(TrainingLocal)
class TrainingLocalAdmin(admin.ModelAdmin):
    list_display = ('name', 'cep', 'address', 'complement', 'state', 'city', 'lat', 'lon',)
    search_fields = ('name', 'cep', 'address', 'complement', 'state', 'city',)


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('local', 'date', 'subscriptions', 'cash')

    def subscriptions(self, obj):
        return obj.subscription_set.count()
    subscriptions.short_description = _('Subscriptions')

    def cash(self, obj):
        ticket = preferences['subscription__ticket_value']
        payers = obj.subscription_set.exclude(payment='eletronic').filter(paid__lt=ticket).count()
        value = ticket * payers
        return 'R$ %s' % format_money(value)
    cash.short_description = _('cash')
