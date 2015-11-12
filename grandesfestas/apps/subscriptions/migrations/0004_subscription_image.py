# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20151110_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='image',
            field=models.ImageField(blank=True, upload_to='subscription'),
        ),
    ]
