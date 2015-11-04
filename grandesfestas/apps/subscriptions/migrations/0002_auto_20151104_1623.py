# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPayment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created_date', models.DateTimeField(verbose_name='Created date', auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('subscription', models.ForeignKey(to='subscriptions.Subscription')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='subscriptionpayment',
            unique_together=set([('subscription', 'content_type', 'object_id')]),
        ),
    ]
