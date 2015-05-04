# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0002_auto_20150504_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='vessel',
        ),
        migrations.AddField(
            model_name='batch',
            name='vessel',
            field=models.ForeignKey(related_name='batches', default=1, to='kombucha_manager.Vessel'),
            preserve_default=False,
        ),
    ]
