# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from subscriptions.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('volunteer', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)
    list_editable = ('training', 'present', 'paid', 'payment', 'valid', 'extra')
    list_filter = ('volunteer', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)
    search_fields = ('volunteer', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)
