# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_subcategory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('choice', models.CharField(max_length=123, blank=True)),
                ('vote', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('required', models.BooleanField(default=True)),
                ('question_type', models.CharField(default=b'text', max_length=200, choices=[(b'text', b'text'), (b'radio', b'radio'), (b'select', b'select'), (b'select-multiple', b'Select Multiple'), (b'integer', b'integer')])),
                ('choices', models.TextField(help_text=b'if the question type is "radio," "select," or "select multiple" provide a comma-separated list of options for this question .', null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, to='category.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=128, blank=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.ForeignKey(to='category.Category')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(to='survey.Survey'),
        ),
        migrations.AddField(
            model_name='choice',
            name='questionId',
            field=models.ForeignKey(related_name='choice', to='survey.Question'),
        ),
    ]
