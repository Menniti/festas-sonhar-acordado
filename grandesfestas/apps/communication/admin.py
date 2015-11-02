# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.urlresolvers import reverse
from django import forms
from django.utils.html import format_html

from suit.widgets import AutosizedTextarea
from suit_redactor.widgets import RedactorWidget
from communication.models import ContactEmail, ScheduledEmail, TemplateEmail


class TemplateEmailForm(forms.ModelForm):
    class Meta:
        model = TemplateEmail
        fields = ('subject', 'sender', 'html_content', 'text_content',)
        widgets = {
            'html_content': RedactorWidget(
                editor_options={'buttons': ['html', '|', 'formatting', '|', 'bold', 'italic']}
            ),
            'text_content': AutosizedTextarea(attrs={'class': 'span-12', 'rows': 10}),
        }


@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    pass


@admin.register(TemplateEmail)
class TemplateEmailAdmin(admin.ModelAdmin):
    form = TemplateEmailForm
    list_display = ('subject', 'created_date', 'modified_date',)
    list_filter = ('created_date', 'modified_date',)
    search_fields = ('subject',)


@admin.register(ScheduledEmail)
class ScheduledEmailAdmin(admin.ModelAdmin):
    list_display = ('template', 'date', 'sent', 'content_type', 'content_object')

    def get_queryset(self, request):
        qs = super(ScheduledEmailAdmin, self).get_queryset(request)
        return qs.select_related('template')
