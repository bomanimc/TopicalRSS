# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0003_rss_episodes_xml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rss_episodes',
            name='xml',
            field=models.CharField(max_length=10000, null=True, blank=True),
        ),
    ]
