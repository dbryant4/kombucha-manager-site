# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0005_auto_20150512_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'batches'},
        ),
        migrations.AlterField(
            model_name='bottle',
            name='size',
            field=models.ForeignKey(related_name='bottles', default=1, to='kombucha_manager.BottleSize'),
            preserve_default=False,
        ),
    ]
