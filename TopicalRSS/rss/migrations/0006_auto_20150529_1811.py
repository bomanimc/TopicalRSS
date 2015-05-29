# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0005_auto_20150521_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='parentFeed',
            field=models.ForeignKey(to='rss.Feed', null=True),
        ),
    ]
