# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_survey_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('response', models.CharField(max_length=66, blank=True)),
                ('question', models.ForeignKey(to='survey.Question')),
                ('survey', models.ForeignKey(to='survey.Survey')),
            ],
        ),
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='survey',
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
