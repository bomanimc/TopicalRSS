# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rss_episodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, blank=True)),
                ('episodeNum', models.IntegerField()),
            ],
        ),
    ]
