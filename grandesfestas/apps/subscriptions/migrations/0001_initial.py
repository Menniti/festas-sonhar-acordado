# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='Created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('present', models.BooleanField(default=False, verbose_name='Present in training')),
                ('paid', models.FloatField(default=0, verbose_name='Paid')),
                ('payment', models.CharField(max_length=16, verbose_name='Payment', blank=True, choices=[('Cash', 'cash'), ('Eletronic', 'eletronic')])),
                ('extra', models.PositiveSmallIntegerField(default=0, verbose_name='Extra value')),
                ('valid', models.BooleanField(default=False, verbose_name='Valid')),
                ('training', models.ForeignKey(to='trainings.Training', verbose_name='Training', blank=True, null=True)),
                ('volunteer', models.ForeignKey(to='volunteers.Volunteer', verbose_name='Volunteer')),
            ],
            options={
                'verbose_name_plural': 'Subscriptions',
                'verbose_name': 'Subscription',
            },
        ),
    ]
