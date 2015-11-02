# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0003_auto_20151102_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactemail',
            name='created_date',
            field=models.DateTimeField(verbose_name='Created date', default=datetime.datetime(2015, 11, 2, 6, 8, 48, 827323, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactemail',
            name='modified_date',
            field=models.DateTimeField(verbose_name='Modified date', default=datetime.datetime(2015, 11, 2, 6, 8, 56, 204432, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='templateemail',
            name='subject',
            field=models.CharField(verbose_name='Subject', max_length=128),
        ),
    ]
