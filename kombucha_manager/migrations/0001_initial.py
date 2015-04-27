# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tea_volume', models.DecimalField(default=0.0, max_digits=5, decimal_places=1)),
                ('sugar_volume', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('brew_volume', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('scoby_count', models.IntegerField(default=1)),
                ('brew_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date of first fermentation')),
                ('comments', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bottle_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'date bottled')),
                ('comments', models.TextField(null=True)),
                ('batch', models.ForeignKey(related_name='bottles', to='kombucha_manager.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('name', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('url', models.CharField(default=b'', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField(null=True)),
                ('source', models.ForeignKey(related_name='teas', to='kombucha_manager.Source')),
            ],
        ),
        migrations.CreateModel(
            name='TeaType',
            fields=[
                ('name', models.CharField(max_length=200, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='tea',
            name='tea_type',
            field=models.ForeignKey(related_name='teas', to='kombucha_manager.TeaType'),
        ),
        migrations.AddField(
            model_name='flavor',
            name='source',
            field=models.ManyToManyField(related_name='flavors', to='kombucha_manager.Source'),
        ),
        migrations.AddField(
            model_name='bottle',
            name='flavors',
            field=models.ManyToManyField(related_name='bottles', to='kombucha_manager.Flavor'),
        ),
        migrations.AddField(
            model_name='batch',
            name='tea',
            field=models.ManyToManyField(related_name='batches', to='kombucha_manager.Tea'),
        ),
    ]
