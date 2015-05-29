# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0002_rss_episodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='rss_episodes',
            name='xml',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
