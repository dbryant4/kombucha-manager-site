# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='url',
            new_name='source_url',
        ),
    ]
