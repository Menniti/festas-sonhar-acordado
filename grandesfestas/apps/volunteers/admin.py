# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from volunteers.models import Volunteer


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'email', 'rg', 'birthdate', 'phone', 'occupation', 'organization', 'cep', 'address', 'complement', 'state', 'city',)
    list_filter = ('created_date', 'modified_date', 'birthdate', 'state', 'city',)
    search_fields = ('name', 'email', 'rg', 'phone', 'occupation', 'organization', 'state', 'city',)
