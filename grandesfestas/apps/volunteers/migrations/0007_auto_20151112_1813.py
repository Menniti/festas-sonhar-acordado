# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0006_auto_20151112_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='birthdate',
            field=models.DateField(verbose_name='Birthdate', null=True),
        ),
    ]
