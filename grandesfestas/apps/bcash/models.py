# -*- coding: utf-8 -*-
import json
from django.db import models
from django.utils.translation import ugettext_lazy as _

ST_WAITING = 0
ST_APPROVED = 1
ST_FAILED = 2


class Transaction(models.Model):
    created_date = models.DateTimeField(_('created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True, editable=False)
    order_id = models.PositiveIntegerField(_('order id'), db_index=True)
    status = models.CharField(_('status'), max_length=24, default='', db_index=True)
    status_code = models.PositiveIntegerField(_('status code'), db_index=True)
    transaction_id = models.PositiveIntegerField(_('transaction id'))
    raw_data = models.TextField(_('raw data'))

    @property
    def json_data(self):
        return json.loads(self.raw_data)
