# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0004_complaint_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
