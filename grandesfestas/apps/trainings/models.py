from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_date = models.DateTimeField(_('Created date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified date'), auto_now=True, editable=False)

    class Meta:
        abstract = True


class TrainingLocal(BaseModel):
    name = models.CharField(_('Name'), max_length=64)
    cep = models.CharField(_('Cep'), max_length=9)
    address = models.CharField(_('Address'), max_length=128)
    complement = models.CharField(_('Complement'), max_length=32)
    state = models.CharField(_('State'), max_length=32)
    city = models.CharField(_('City'), max_length=32)
    lat = models.FloatField(_('Latitude'), default=0)
    lon = models.FloatField(_('Longitude'), default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Training local')
        verbose_name_plural = _('Training locals')


class Training(BaseModel):
    local = models.ForeignKey(TrainingLocal, verbose_name=_('Local'))
    date = models.DateTimeField(_('Date'), )

    def __unicode__(self):
        return self.local.__unicode__()

    class Meta:
        verbose_name = _('Training')
        verbose_name_plural = _('Trainings')

