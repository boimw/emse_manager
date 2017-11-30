# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0007_auto_20171125_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
