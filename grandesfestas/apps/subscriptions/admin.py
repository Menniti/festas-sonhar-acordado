# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from subscriptions.models import Subscription


class PatchAbleModelAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super(PatchAbleModelAdmin, self).get_fields(request, obj=obj)
        if request.POST.get('_method') == 'PATCH':
            return [f for f in fields if f in request.POST]
        return fields

    def _patchable_toggle_field(self, field, obj):
        img = static("admin/img/icon-") + '%s.gif'
        elid = '%s_%s_%s_%d' % (obj._meta.app_label, obj._meta.model_name, field, obj.id,)
        jsfn = ''.join([
            "django.jQuery.post('", obj.get_absolute_url(), "'"
            ",{'_method':'PATCH'",
            ",'id':", str(obj.id),
            ",'csrfmiddlewaretoken':document.cookie.match(/csrftoken=(\w+)/)[1]",
            ",'", field, "': django.jQuery('#", elid, "').attr('src').endsWith('no.gif')"
            "}).progress(function(){ ",
            "django.jQuery('#", elid, "').attr('src',",
            "'", img, "'.replace(/%s/, 'clock')) })",
            ".success(function(r){",
            "django.jQuery('#", elid, "').attr('src',",
            "'", img, "'.replace(/%s/, r.", field, "?'yes':'no')) })"
        ])

        return format_html(
            '<img id="{}" onclick="{}" src="{}" style="cursor:pointer"/>',
            elid,
            jsfn,
            img % ('yes' if getattr(obj, field) else 'no')
        )


@admin.register(Subscription)
class SubscriptionAdmin(PatchAbleModelAdmin):
    list_display = ('volunteer', 'created_date', 'modified_date', 'training', 'list_present', 'paid', 'payment', 'list_valid', 'extra',)
    list_filter = ('volunteer', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)
    search_fields = ('volunteer', 'created_date', 'modified_date', 'training', 'present', 'paid', 'payment', 'valid', 'extra',)

    def list_present(self, obj):
        return self._patchable_toggle_field('present', obj)

    def list_valid(self, obj):
        return self._patchable_toggle_field('valid', obj)
