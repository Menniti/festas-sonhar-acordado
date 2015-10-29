# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_auto_20151022_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='payment',
            field=models.CharField(blank=True, choices=[('aps1', 'Amigos para Sempre 1'), ('aps2', 'Amigos para Sempre 2'), ('aps3', 'Amigos para Sempre 3'), ('aps4', 'Amigos para Sempre 4'), ('aps5', 'Amigos para Sempre 5'), ('sj', 'Sonhando Juntos'), ('ppf', 'Preparando para o Futuro')], max_length=16, verbose_name='Project'),
        ),
    ]
