# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20161124_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=datetime.datetime(2016, 11, 25, 6, 17, 45, 24783, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
    ]
