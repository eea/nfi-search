# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20180613_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='nuts_levels',
            field=models.ManyToManyField(db_table='document_nuts_level', related_name='documents', to='search.DNutsLevel'),
        ),
    ]
