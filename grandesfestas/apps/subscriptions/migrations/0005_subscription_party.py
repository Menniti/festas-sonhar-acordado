# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_subscription_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='party',
            field=models.BooleanField(verbose_name='Present in party', default=False),
        ),
    ]
