# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=233, blank=True)),
                ('body', models.TextField()),
                ('category_id', models.CharField(max_length=122, blank=True)),
                ('against_id', models.CharField(max_length=122, blank=True)),
                ('anonymous', models.BooleanField(default=True)),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('closedDate', models.DateTimeField()),
                ('user', models.CharField(max_length=12, blank=True)),
                ('assignedTo', models.CharField(max_length=122, blank=True)),
                ('priority', models.CharField(max_length=10, blank=True)),
            ],
        ),
    ]
