# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.management import update_contenttypes
from django.db import migrations, models

TRAINING_HTML_TPL = """Bom dia!
<p>Este email é para lembrar que o dia do seu treinamento está chegando!</p>
<p>Tome nota da data e local:</p>

<table>
<tbody><tr>
<td>Local:</td><td>{{ training.local.name }}</td>
</tr>
<tr>
<td>Endereço:</td><td>
    {{ training.local.address }}<br>
    {{ training.local.city }}/{{ training.local.state }}
    </td>
</tr>
<tr>
<td>Data:</td><td>{{ training.date }}</td>
</tr>
</tbody></table>

Forte abraço,"""

TRAINING_TEXT_TPL = """Bom dia!

Este email é para lembrar que o dia do seu treinamento está chegando!

Tome nota da data e local:

* Local:    {{ training.local.name }}
* Endereço: {{ training.local.address }}, {{ training.local.city }}/{{ training.local.state }}
* Data: {{ training.date }}

Forte abraço,"""

SUBSCRIPTION_HTML_TPL = """Olá {{ subscription.volunteer.first_name }}<br><br>
Nós estamos muito felizes com sua inscrição e esperamos que você também esteja.
Queremos<br>lembrá-lo que ainda falta um detalhe para completar sua inscrição,
que comparecer no dia do<br>treinamento que você escolheu.<br><p><br></p>
<table>
<thead><tr><th colspan="2">Treinamento</th></tr></thead>
<tbody><tr>
<td>Nome do local:</td><td>{{ subscription.training.local.name }}</td>
</tr>
<tr>
<td>Endereço:</td><td>
    {{ subscription.training.local.address }}<br>
    {{ subscription.training.local.city }}/{{ subscription.training.local.state }}
    </td>
</tr>
<tr>
<td>Data:</td><td>{{ subscription.training.date }}</td>
</tr>
</tbody></table>

Forte abraço,"""

SUBSCRIPTION_TEXT_TPL = """Olá {{ subscription.volunteer.first_name }}

Nós estamos muito felizes com sua inscrição e esperamos que você também esteja. Queremos
lembrá-lo que ainda falta um detalhe para completar sua inscrição, que comparecer no dia do
treinamento que você escolheu.

Treinamento
-----------------

* Nome do local: {{ subscription.training.local.name }}
* Endereço: {{ subscription.training.local.address }}, {{ subscription.training.local.city }}/{{ subscription.training.local.state }}
* Data: {{ subscription.training.date }}

Forte abraço,"""


def create_initial_templates(apps, schema_editor):
    ContentType = apps.get_model("contenttypes", "ContentType")
    TemplateEmail = apps.get_model("communication", "TemplateEmail")

    Subscription, new = ContentType.objects.get_or_create(app_label='trainings', model='training')
    Training, new = ContentType.objects.get_or_create(app_label='subscriptions', model='subscription')

    if not TemplateEmail.objects.filter(content_type=Training).exists():
        TemplateEmail.objects.create(
            subject='Seu treinamento está chegando!',
            html_content=TRAINING_HTML_TPL,
            text_content=TRAINING_TEXT_TPL,
            sender='voluntarios@sonharacordado.com.br',
            content_type=Training
        )

    if not TemplateEmail.objects.filter(content_type=Subscription).exists():
        TemplateEmail.objects.create(
            subject='Inscrição para Festa de Natal 2015!',
            html_content=SUBSCRIPTION_HTML_TPL,
            text_content=SUBSCRIPTION_TEXT_TPL,
            sender='voluntarios@sonharacordado.com.br',
            content_type=Subscription
        )


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0003_initial_data'),
        ('subscriptions', '0002_auto_20151104_1623'),
        ('communication', '0005_templateemail_content_type'),
    ]

    operations = [
        migrations.RunPython(create_initial_templates),
    ]
