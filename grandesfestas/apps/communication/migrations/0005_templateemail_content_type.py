# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def set_training_template_as_initial(apps, schema_editor):
    ContentType = apps.get_model("contenttypes", "ContentType")
    TemplateEmail = apps.get_model("communication", "TemplateEmail")
    default = ContentType.objects.get(app_label='trainings', model='training')
    TemplateEmail.objects.update(content_type=default)


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('communication', '0004_auto_20151102_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='templateemail',
            name='content_type',
            field=models.OneToOneField(to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.RunPython(set_training_template_as_initial)
    ]
