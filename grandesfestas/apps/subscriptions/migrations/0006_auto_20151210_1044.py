# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_subscription_party'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='party',
        ),
        migrations.AddField(
            model_name='subscription',
            name='bracelet',
            field=models.CharField(blank=True, verbose_name='Bracelet Code', max_length=64),
        ),
    ]
