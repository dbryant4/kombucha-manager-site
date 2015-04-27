# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0003_auto_20150426_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tea',
            old_name='source',
            new_name='sources',
        ),
        migrations.RenameField(
            model_name='tea',
            old_name='tea_type',
            new_name='tea_types',
        ),
    ]
