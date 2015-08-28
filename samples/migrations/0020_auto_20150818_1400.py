# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0019_auto_20150817_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='acad_loc',
            new_name='acad_location',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='accession_date',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='collection_details',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='collection_notes',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='details',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='other_notes',
        ),
        migrations.AddField(
            model_name='sample',
            name='date_of_entry',
            field=models.DateField(null=True, verbose_name='Date of entry into ACAD'),
        ),
        migrations.AddField(
            model_name='sample',
            name='genus',
            field=models.CharField(max_length=255, verbose_name='Genus', blank=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='species',
            field=models.CharField(max_length=255, verbose_name='Species', blank=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='subspecies',
            field=models.CharField(max_length=255, verbose_name='Subspecies', blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='category',
            field=models.CharField(max_length=255, verbose_name='Category of sample'),
        ),
    ]
