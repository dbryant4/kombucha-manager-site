# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0006_auto_20150512_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='discarded',
            field=models.BooleanField(default=False),
        ),
    ]
