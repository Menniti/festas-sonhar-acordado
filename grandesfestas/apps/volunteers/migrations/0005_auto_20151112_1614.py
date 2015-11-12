# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0004_auto_20151029_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='project',
            field=models.CharField(blank=True, choices=[('aps1', 'Amigos para Sempre 1'), ('aps2', 'Amigos para Sempre 2'), ('aps3', 'Amigos para Sempre 3'), ('aps4', 'Amigos para Sempre 4'), ('aps5', 'Amigos para Sempre 5'), ('sj', 'Sonhando Juntos'), ('ppf1', 'Preparando para o Futuro (Frei Tito)'), ('ppf2', 'Preparando para o Futuro (Caritas)'), ('cs', 'Contando Sonhos')], verbose_name='Project', max_length=16),
        ),
    ]
