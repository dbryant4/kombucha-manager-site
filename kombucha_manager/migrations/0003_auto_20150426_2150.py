# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0002_auto_20150426_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='brew_date',
            field=models.DateField(default=datetime.datetime.today, verbose_name=b'date of first fermentation'),
        ),
        migrations.AlterField(
            model_name='bottle',
            name='bottle_date',
            field=models.DateField(default=datetime.datetime.today, verbose_name=b'date bottled'),
        ),
        migrations.RemoveField(
            model_name='tea',
            name='source',
        ),
        migrations.AddField(
            model_name='tea',
            name='source',
            field=models.ManyToManyField(related_name='teas', to='kombucha_manager.Source'),
        ),
        migrations.RemoveField(
            model_name='tea',
            name='tea_type',
        ),
        migrations.AddField(
            model_name='tea',
            name='tea_type',
            field=models.ManyToManyField(related_name='teas', to='kombucha_manager.TeaType'),
        ),
    ]
