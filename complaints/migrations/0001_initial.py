# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=233, blank=True)),
                ('body', models.TextField()),
                ('against_id', models.CharField(max_length=122, blank=True)),
                ('anonymous', models.BooleanField(default=True)),
                ('closedDate', models.DateField(blank=True)),
                ('assignedTo', models.CharField(max_length=122, blank=True)),
                ('category_id', models.ForeignKey(to='category.Category')),
            ],
        ),
    ]
