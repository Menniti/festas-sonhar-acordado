# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import now, timedelta


def load_initial_data(apps, schema_editor):
    Training = apps.get_model("trainings", "Training")
    TrainingLocal = apps.get_model("trainings", "TrainingLocal")

    local = TrainingLocal.objects.create(
        name='Sede do Sonhar Acordado',
        cep='05609-060',
        address='Rua Maestro João Nunes, 30',
        state='SP',
        city='São Paulo'
    )

    Training.objects.create(local=local, date=(now() - timedelta(7))),
    Training.objects.create(local=local, date=now()),
    Training.objects.create(local=local, date=(now() + timedelta(7))),


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0002_auto_20151022_1940'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
