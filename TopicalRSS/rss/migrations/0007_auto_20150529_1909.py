# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0006_auto_20150529_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='feed',
            name='description',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='url',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
