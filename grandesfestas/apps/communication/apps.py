# -*- coding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommunicationConfig(AppConfig):
    name = 'communication'
    verbose_name = _('Communication')

    def ready(self):
        import communication.signals
