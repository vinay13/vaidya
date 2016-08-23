# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_auto_20160819_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.PositiveSmallIntegerField(default=1, choices=[(3, 'Assigned'), (2, 'Closed'), (1, 'Open'), (4, 'Reopen')]),
        ),
    ]
