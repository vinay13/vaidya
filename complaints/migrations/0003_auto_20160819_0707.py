# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0002_auto_20160819_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='against_id',
            field=models.ForeignKey(related_name='Against', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='assignedTo',
            field=models.ForeignKey(related_name='AssignedTo', to=settings.AUTH_USER_MODEL),
        ),
    ]
