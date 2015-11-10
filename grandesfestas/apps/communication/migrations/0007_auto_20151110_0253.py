# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0006_auto_20151105_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactemail',
            options={'verbose_name': 'Contact Email', 'verbose_name_plural': 'Contact Emails'},
        ),
        migrations.AlterModelOptions(
            name='scheduledemail',
            options={'verbose_name': 'Scheduled Email', 'verbose_name_plural': 'Scheduled Emails'},
        ),
        migrations.AlterModelOptions(
            name='templateemail',
            options={'verbose_name': 'Template Email', 'verbose_name_plural': 'Templates Emails'},
        ),
    ]
