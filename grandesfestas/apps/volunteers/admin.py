# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from import_export.admin import ExportMixin
from volunteers.models import Volunteer
from volunteers import resources


@admin.register(Volunteer)
class VolunteerAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'created_date', 'email', 'rg', 'birthdate', 'phone', 'occupation', 'organization', 'cep', 'address', 'complement', 'state', 'city', 'project')
    list_filter = ('created_date', 'modified_date', 'birthdate', 'state', 'city', 'project',)
    search_fields = ('name', 'email', 'rg', 'phone', 'occupation', 'organization', 'state', 'city',)
    resource_class = resources.VolunteerResource
