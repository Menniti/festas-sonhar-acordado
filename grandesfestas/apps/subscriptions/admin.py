# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ExportMixin
from subscriptions.models import Subscription
from subscriptions import resources


@admin.register(Subscription)
class SubscriptionAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('volunteer', 'volunteer__project', 'created_date', 'modified_date', 'training', 'present', 'bracelet', 'paid', 'payment', 'valid', 'extra',)
    list_editable = ('training', 'present', 'bracelet', 'paid', 'payment', 'valid', 'extra')
    list_filter = ('volunteer', 'volunteer__project', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)
    search_fields = ('volunteer__name', 'volunteer__email', 'bracelet',)
    resource_class = resources.SubscriptionResource

    def volunteer__project(self, obj):
        return obj.volunteer.project
    volunteer__project.short_description = _('Project')

    def get_queryset(self, request):
        queryset = super(SubscriptionAdmin, self).get_queryset(request)
        return queryset.select_related('volunteer')
