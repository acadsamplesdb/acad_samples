# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_extracted', models.DateField(verbose_name='Date extracted')),
                ('extracted_by', models.CharField(verbose_name='Extracted by', max_length=255)),
                ('method', models.TextField(verbose_name='Extraction method')),
                ('starting', models.CharField(verbose_name='Details of starting material', max_length=255)),
                ('final_vol', models.CharField(verbose_name='Final DNA volume (in ul)', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, verbose_name='NCBI taxonomy ID', serialize=False)),
                ('genus', models.CharField(verbose_name='Genus', blank=True, max_length=255)),
                ('species', models.CharField(verbose_name='Species', blank=True, max_length=255)),
                ('subspecies', models.CharField(verbose_name='Subspecies', blank=True, max_length=255)),
                ('common', models.CharField(verbose_name='Common name', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Project title', max_length=255)),
                ('description', models.TextField(verbose_name='Project description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('acad_num', models.AutoField(serialize=False, primary_key=True, verbose_name='ACAD sample number')),
                ('other_num', models.CharField(verbose_name='Other sample number', blank=True, max_length=255)),
                ('description', models.CharField(verbose_name='Sample description', max_length=255)),
                ('category', models.CharField(choices=[('bone', 'Bone'), ('tooth', 'Tooth'), ('skin', 'Skin'), ('tissue', 'Tissue (all non-skin)'), ('feather', 'Feather'), ('horn', 'Horn'), ('egg', 'Egg'), ('sediment', 'Sediment'), ('ice', 'Ice'), ('hair', 'Hair'), ('coprolite', 'Coprolite'), ('insect', 'Insect'), ('mollusc', 'Mollusc'), ('vegetation', 'Vegetation'), ('wood', 'Wood'), ('seed', 'Seed (includes fruit)'), ('other', 'Other'), ('extractcontrol', 'Extraction control')], verbose_name='Category of sample', max_length=255)),
                ('acad_loc', models.CharField(verbose_name='ACAD location', blank=True, max_length=255)),
                ('accession_date', models.DateField(verbose_name='Date of entry into ACAD')),
                ('abc_num', models.CharField(verbose_name='ABC/Oxford sample number', blank=True, max_length=255)),
                ('details', models.CharField(verbose_name='Sample details', blank=True, max_length=255)),
                ('notes', models.TextField(verbose_name='Sample notes', blank=True)),
                ('region', models.CharField(verbose_name='Region', blank=True, max_length=255)),
                ('country', models.CharField(verbose_name='Country', blank=True, max_length=255)),
                ('state', models.CharField(verbose_name='State', blank=True, max_length=255)),
                ('locality', models.CharField(verbose_name='Locality', blank=True, max_length=255)),
                ('location', models.CharField(verbose_name='Specific location', blank=True, max_length=255)),
                ('lat', models.FloatField(verbose_name='Latitude', blank=True, null=True)),
                ('lon', models.FloatField(verbose_name='Longitude', blank=True, null=True)),
                ('collection_details', models.CharField(verbose_name='Collecton details', blank=True, max_length=255)),
                ('collection_notes', models.CharField(verbose_name='Collection notes', blank=True, max_length=255)),
                ('collection_date', models.DateField(verbose_name='Collection date', blank=True, null=True)),
                ('collected_by', models.CharField(verbose_name='Collected by', blank=True, max_length=255)),
                ('museum', models.CharField(verbose_name='Museum name', blank=True, max_length=255)),
                ('museum_num', models.CharField(verbose_name='Museum accession number', blank=True, max_length=255)),
                ('sampled_by', models.CharField(verbose_name='Sampled by', blank=True, max_length=255)),
                ('sample_date', models.DateField(verbose_name='Date sampled', blank=True, null=True)),
                ('organism', models.ForeignKey(null=True, blank=True, to='samples.Organism')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='samples',
            field=models.ManyToManyField(to='samples.Sample'),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='extraction',
            name='extract_control',
            field=models.ManyToManyField(related_name='controls', blank=True, to='samples.Sample'),
        ),
        migrations.AddField(
            model_name='extraction',
            name='sample',
            field=models.ManyToManyField(to='samples.Sample'),
        ),
    ]
