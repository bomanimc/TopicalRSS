# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0007_auto_20150529_1909'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestModel',
        ),
    ]
