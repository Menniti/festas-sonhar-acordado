# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_remove_templateemail_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templateemail',
            name='sender',
            field=models.EmailField(verbose_name='From', max_length=254, default='fabio.montefuscolo@hacklab.com.br'),
        ),
    ]
