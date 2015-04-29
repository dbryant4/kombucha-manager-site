# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0004_auto_20150426_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('name', models.CharField(max_length=200, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='vessel',
            field=models.ManyToManyField(related_name='batches', to='kombucha_manager.Vessel'),
        ),
    ]
