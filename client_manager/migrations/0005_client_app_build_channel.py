# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 13:23
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('devicemanager', '0006_auto_20170116_1853'),
        ('client_manager', '0004_auto_20170114_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='app_build_channel',
            field=models.ForeignKey(blank=True,
                                    help_text='All devices owned by this client will recieve updates published to this channel.',
                                    null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='devicemanager.AppBuildChannel'),
        ),
    ]
