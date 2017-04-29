# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('feedmanager', '0002_auto_20160821_1855'),
    ]

    operations = [
        migrations.AddField(
                model_name='template',
                name='duration',
                field=models.PositiveIntegerField(
                        default=10000,
                        help_text='How long should a slide using this template be visible on '
                                  'screen. \nIf a template has an animation this time should '
                                  'ensure that the animation has enough time to complete. '),
        ),
    ]