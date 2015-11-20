# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils import numberformat
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from dynamic_preferences import global_preferences_registry
from trainings.models import Training, TrainingLocal

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
    list_display = ('local', 'date', 'hidden', 'subscriptions', 'cash')
    list_editable = ('hidden',)

    def subscriptions(self, obj):
        counter = obj.subscription_set.count()

        if counter > 0:
            query = {'training__id__exact': obj.id}
            return format_html(
                '<a href="{}?{}">{}</a>',
                reverse('admin:subscriptions_subscription_changelist'),
                urlencode(query),
                counter
            )
        return counter
    subscriptions.short_description = _('Subscriptions')

    def cash(self, obj):
        ticket = preferences['subscription__ticket_value']
        payers = obj.subscription_set.exclude(payment='eletronic').filter(paid__lt=ticket).count()
        value = ticket * payers
        return 'R$ %s' % format_money(value)
    cash.short_description = _('cash')
