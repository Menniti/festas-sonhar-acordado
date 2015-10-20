from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """ Add created_date and modified_date in models that extends this class """

    created_date = models.DateTimeField(_('Created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True, editable=False)

    class Meta:
        abstract = True


class TrainingLocal(BaseModel):
    """ A place where a Training session happens """
    name = models.CharField(_('Name'), max_length=64)
    cep = models.CharField(_('Cep'), max_length=9)
    address = models.CharField(_('Address'), max_length=128)
    complement = models.CharField(_('Complement'), max_length=32, blank=True)
    state = models.CharField(_('State'), max_length=32)
    city = models.CharField(_('City'), max_length=32)
    lat = models.FloatField(_('Latitude'), default=0)
    lon = models.FloatField(_('Longitude'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Training local')
        verbose_name_plural = _('Training locals')


class Training(BaseModel):
    """ Represents a Training session """
    local = models.ForeignKey(TrainingLocal, verbose_name=_('Local'))
    date = models.DateTimeField(_('Date'), )

    def __str__(self):
        date = timezone.localtime(self.date)
        return '%s, %s' % (self.local.name, date.strftime('%d/%m/%Y, %H:%M, %Z'))

    class Meta:
        verbose_name = _('Training')
        verbose_name_plural = _('Trainings')
