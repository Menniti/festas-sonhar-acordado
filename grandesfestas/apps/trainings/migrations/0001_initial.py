# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(verbose_name='Created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='Modified date', auto_now=True)),
                ('date', models.DateTimeField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Training',
                'verbose_name_plural': 'Trainings',
            },
        ),
        migrations.CreateModel(
            name='TrainingLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(verbose_name='Created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(verbose_name='Modified date', auto_now=True)),
                ('name', models.CharField(verbose_name='Name', max_length=64)),
                ('cep', models.CharField(verbose_name='Cep', max_length=9)),
                ('address', models.CharField(verbose_name='Address', max_length=128)),
                ('complement', models.CharField(verbose_name='Complement', max_length=32)),
                ('state', models.CharField(verbose_name='State', max_length=32)),
                ('city', models.CharField(verbose_name='City', max_length=32)),
                ('lat', models.FloatField(default=0, verbose_name='Latitude')),
                ('lon', models.FloatField(default=0, verbose_name='Longitude')),
            ],
            options={
                'verbose_name': 'Training local',
                'verbose_name_plural': 'Training locals',
            },
        ),
        migrations.AddField(
            model_name='training',
            name='local',
            field=models.ForeignKey(to='trainings.TrainingLocal', verbose_name='Local'),
        ),
    ]
