# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_document_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='document',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='search.Document'),
        ),
    ]
