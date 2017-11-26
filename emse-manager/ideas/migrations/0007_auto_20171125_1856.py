# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='idea',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='idea',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]
