# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
