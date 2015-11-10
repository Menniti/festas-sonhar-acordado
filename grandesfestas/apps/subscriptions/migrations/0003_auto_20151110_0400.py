# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20151104_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='payment',
            field=models.CharField(choices=[('cash', 'cash'), ('eletronic', 'eletronic')], blank=True, max_length=16, verbose_name='Payment'),
        ),
    ]
