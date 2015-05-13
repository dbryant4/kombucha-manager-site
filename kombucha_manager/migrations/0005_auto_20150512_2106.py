# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0004_auto_20150512_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bottle',
            old_name='volume',
            new_name='size',
        ),
    ]
