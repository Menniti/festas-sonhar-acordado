from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from volunteers.models import Volunteer


class BaseModel(models.Model):
    """ Add created_date and modified_date in models that extends this class """

    created_date = models.DateTimeField(_('Created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True, editable=False)

    class Meta:
        abstract = True


class ContactEmail(BaseModel):
    email = models.EmailField()
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    content = models.TextField()


class TemplateEmail(BaseModel):
    text_content = models.TextField(_('Text content'))
    html_content = models.TextField(_('HTML content'))
    subject = models.CharField(_('Subject'), max_length=128)
    sender = models.EmailField(_('From'), default=getattr(settings, 'DEFAULT_FROM_EMAIL', ''))
    content_type = models.OneToOneField(ContentType)

    def __str__(self):
        return self.subject


class ScheduledEmail(BaseModel):
    date = models.DateField(_('Date'))
    sent = models.DateTimeField(_('Sent'), null=True, blank=True)
    template = models.ForeignKey(TemplateEmail)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
