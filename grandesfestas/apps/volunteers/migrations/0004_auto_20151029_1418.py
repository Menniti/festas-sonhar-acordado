# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_volunteer_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='payment',
            new_name='project',
        ),
    ]
