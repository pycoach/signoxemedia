# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('mediamanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('device_id', models.UUIDField()),
                ('name', models.CharField(max_length=255)),
                ('last_ping', models.DateTimeField()),
                ('debug_mode', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('feed', models.ForeignKey(blank=True, null=True,
                                           on_delete=django.db.models.deletion.CASCADE,
                                           to='mediamanager.ContentFeed')),
            ],
            options={
                'verbose_name_plural': 'Device Groups',
                'verbose_name': 'Device Group',
            },
        ),
        migrations.CreateModel(
            name='DeviceLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Device Locations',
                'verbose_name': 'Device Location',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='devicemanager.DeviceGroup'),
        ),
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='devicemanager.DeviceLocation'),
        ),
    ]
