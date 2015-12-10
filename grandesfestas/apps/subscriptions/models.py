# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from volunteers.models import Volunteer
from trainings.models import Training


class Subscription(models.Model):
    PAYMENT = (
        ('cash', _("cash")),
        ('eletronic', _("eletronic")),
    )
    created_date = models.DateTimeField(_('Created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True, editable=False)

    volunteer = models.ForeignKey(Volunteer, verbose_name=_('Volunteer'))
    training = models.ForeignKey(Training, verbose_name=_('Training'), null=True, blank=True)
    present = models.BooleanField(_('Present in training'), default=False)
    paid = models.FloatField(_('Paid'), default=0)
    bracelet = models.CharField(_('Bracelet Code'), max_length=64, blank=True)
    payment = models.CharField(_('Payment'), choices=PAYMENT, max_length=16, blank=True)
    extra = models.PositiveSmallIntegerField(_('Extra value'), default=0)
    valid = models.BooleanField(_('Valid'), default=False)
    image = models.ImageField(upload_to='subscription', blank=True)

    def get_absolute_url(self):
        if self.id:
            return reverse('api:subscription-detail', args=[self.id])
        return reverse('api:subscription-list')

    class Meta:
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')


class SubscriptionPayment(models.Model):
    created_date = models.DateTimeField(_('Created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True, editable=False)

    subscription = models.ForeignKey(Subscription)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = (('subscription', 'content_type', 'object_id'),)
