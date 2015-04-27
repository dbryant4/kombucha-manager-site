# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='brew_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'date of first fermentation'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='comments',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bottle',
            name='bottle_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'date bottled'),
        ),
        migrations.AlterField(
            model_name='bottle',
            name='comments',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='flavor',
            name='comments',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tea',
            name='comments',
            field=models.TextField(null=True, blank=True),
        ),
    ]
