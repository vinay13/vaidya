# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_remove_survey_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('response', models.CharField(max_length=66, blank=True)),
                ('question', models.ForeignKey(to='survey.Question')),
                ('survey', models.ForeignKey(to='survey.Survey')),
            ],
        ),
    ]
