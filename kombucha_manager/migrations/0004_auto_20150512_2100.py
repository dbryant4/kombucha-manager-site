# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kombucha_manager', '0003_auto_20150504_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottleSize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='bottle',
            name='volume',
            field=models.ForeignKey(related_name='bottles', blank=True, to='kombucha_manager.BottleSize', null=True),
        ),
    ]
