# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('email', models.EmailField(max_length=254, verbose_name='Email', unique=True)),
                ('name', models.CharField(verbose_name='Name', max_length=64)),
                ('rg', models.CharField(verbose_name='Rg', max_length=16)),
                ('birthdate', models.DateField(verbose_name='Birthdate')),
                ('phone', models.CharField(verbose_name='Phone', max_length=32)),
                ('occupation', models.CharField(verbose_name='Occupation', max_length=32)),
                ('organization', models.CharField(verbose_name='Organization', max_length=32)),
                ('cep', models.CharField(verbose_name='Cep', max_length=9)),
                ('address', models.CharField(verbose_name='Address', max_length=128)),
                ('complement', models.CharField(verbose_name='Complement', max_length=32)),
                ('state', models.CharField(verbose_name='State', max_length=32)),
                ('city', models.CharField(verbose_name='City', max_length=32)),
            ],
            options={
                'verbose_name': 'Volunteer',
                'verbose_name_plural': 'Volunteers',
            },
        ),
    ]
