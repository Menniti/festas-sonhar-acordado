# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from import_export.admin import ExportMixin
from subscriptions.models import Subscription
from subscriptions import resources


@admin.register(Subscription)
class SubscriptionAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('volunteer', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)
    list_editable = ('training', 'present', 'paid', 'payment', 'valid', 'extra')
    list_filter = ('volunteer', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)
    search_fields = ('volunteer__name', 'volunteer__email')
    resource_class = resources.SubscriptionResource
