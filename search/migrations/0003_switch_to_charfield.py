# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_fix_relations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countrydata',
            options={'verbose_name_plural': 'CountryData'},
        ),
        migrations.AlterModelOptions(
            name='ddataset',
            options={'verbose_name_plural': 'DDataSets'},
        ),
        migrations.AlterModelOptions(
            name='ddatasource',
            options={'verbose_name_plural': 'DDataSources'},
        ),
        migrations.AlterModelOptions(
            name='ddatatype',
            options={'verbose_name_plural': 'DDataTypes'},
        ),
        migrations.AlterModelOptions(
            name='dfiletype',
            options={'verbose_name_plural': 'DFileTypes'},
        ),
        migrations.AlterModelOptions(
            name='dinfolevel',
            options={'verbose_name_plural': 'DInfoLevels'},
        ),
        migrations.AlterModelOptions(
            name='dkeyword',
            options={'verbose_name_plural': 'DKeywords'},
        ),
        migrations.AlterModelOptions(
            name='dlanguage',
            options={'verbose_name_plural': 'DLanguages'},
        ),
        migrations.AlterModelOptions(
            name='dnutslevel',
            options={'verbose_name_plural': 'DNutsLevels'},
        ),
        migrations.AlterModelOptions(
            name='documentkeyword',
            options={'verbose_name_plural': 'DocumentKeywords'},
        ),
        migrations.AlterModelOptions(
            name='documentnutslevel',
            options={'verbose_name_plural': 'DocumentNutsLevels'},
        ),
        migrations.AlterModelOptions(
            name='dresourcetype',
            options={'verbose_name_plural': 'DResourceTypes'},
        ),
        migrations.AlterModelOptions(
            name='dtopiccategory',
            options={'verbose_name_plural': 'DTopicCategories'},
        ),
        migrations.AlterModelOptions(
            name='filelanguage',
            options={'verbose_name_plural': 'FileLanguages'},
        ),
        migrations.AlterModelOptions(
            name='geographicbounds',
            options={'verbose_name_plural': 'GeographicBounds'},
        ),
        migrations.AlterField(
            model_name='countrydata',
            name='contact_email',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='countrydata',
            name='country_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='countrydata',
            name='country_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='countrydata',
            name='source_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='countrydata',
            name='source_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='dcountry',
            name='code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dcountry',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='ddataset',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='ddatasource',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='ddatatype',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='dfiletype',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='dinfolevel',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='dkeyword',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='dlanguage',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='dnutslevel',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='dresourcetype',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='dtopiccategory',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='responsible_person',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]