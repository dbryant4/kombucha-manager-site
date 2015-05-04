# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
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
                ('brew_date', models.DateField(default=datetime.datetime.today, verbose_name=b'date of first fermentation')),
                ('comments', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bottle_date', models.DateField(default=datetime.datetime.today, verbose_name=b'date bottled')),
                ('comments', models.TextField(null=True, blank=True)),
                ('batch', models.ForeignKey(related_name='bottles', to='kombucha_manager.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('comments', models.TextField(null=True, blank=True)),
                ('sources', models.ManyToManyField(related_name='teas', to='kombucha_manager.Source')),
            ],
        ),
        migrations.CreateModel(
            name='TeaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(related_name='user_profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(related_name='user_profiles', to='kombucha_manager.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('organization', models.ForeignKey(related_name='vessels', to='kombucha_manager.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='tea',
            name='tea_types',
            field=models.ManyToManyField(related_name='teas', to='kombucha_manager.TeaType'),
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
        migrations.AddField(
            model_name='batch',
            name='vessel',
            field=models.ManyToManyField(related_name='batches', to='kombucha_manager.Vessel'),
        ),
    ]
