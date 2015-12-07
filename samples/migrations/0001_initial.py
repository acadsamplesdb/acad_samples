# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amplification',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('prepared_by', models.CharField(verbose_name='Prepared by', max_length=255)),
                ('method', models.TextField(verbose_name='Method', help_text='e.g. library prep or PCR')),
                ('amp_type', models.CharField(verbose_name='Amplification type', max_length=255, blank=True)),
                ('treatment', models.CharField(verbose_name='Treatment', max_length=255, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AmplificationResult',
            fields=[
                ('id', models.CharField(serialize=False, max_length=255, blank=True, primary_key=True)),
                ('dna_yield', models.PositiveIntegerField(blank=True, null=True)),
                ('quant_method', models.CharField(verbose_name='Quantification method', max_length=255, blank=True)),
                ('amplification', models.ForeignKey(to='samples.Amplification')),
            ],
        ),
        migrations.CreateModel(
            name='AQISSampleGroup',
            fields=[
                ('group_num', models.CharField(verbose_name='Group number', serialize=False, max_length=255, blank=True, primary_key=True)),
                ('group_num_int', models.PositiveIntegerField(blank=True, null=True)),
                ('aqis_num', models.CharField(verbose_name='AQIS Quarantine Entry/Order Number', max_length=255, blank=True)),
                ('accession_date', models.DateField(verbose_name='Date of entry into ACAD', blank=True, null=True)),
                ('permit_num', models.CharField(verbose_name='Permit number', max_length=255, blank=True)),
                ('description', models.CharField(verbose_name='Goods description', max_length=255, blank=True)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Quantity', blank=True, null=True)),
                ('origin', models.CharField(verbose_name='Country of origin', max_length=255, blank=True)),
                ('acad_loc', models.CharField(verbose_name='ACAD location', max_length=255, blank=True)),
                ('movement', models.CharField(verbose_name='Movement and transfer', max_length=255, blank=True)),
                ('notes', models.CharField(verbose_name='Other relevant info', max_length=255, blank=True)),
                ('sent_by', models.CharField(verbose_name='Sent by', max_length=255, blank=True)),
                ('contact', models.CharField(verbose_name='ACAD contact', max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'AQIS sample group',
                'ordering': ['-group_num_int', '-group_num'],
            },
        ),
        migrations.CreateModel(
            name='C14',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sampref', models.CharField(max_length=255)),
                ('date', models.CharField(verbose_name='Estimated age in radiocarbon years', max_length=255)),
                ('error', models.PositiveSmallIntegerField(verbose_name='Estimated carbon date error range', blank=True, null=True)),
                ('centre', models.CharField(verbose_name='Centre that did carbon dating', max_length=255)),
                ('centre_num', models.CharField(verbose_name='Centre reference number', max_length=255)),
                ('del13', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('del15', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('cnratio', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('use_weight', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('pyield', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('burnweight', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('burnyield', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('pcbyield', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('nyield', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('percent_c', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('mg_c', models.DecimalField(decimal_places=20, max_digits=25, blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enrichment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Date')),
                ('prepared_by', models.CharField(verbose_name='Prepared by', max_length=255)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EnrichmentResult',
            fields=[
                ('id', models.CharField(serialize=False, max_length=255, blank=True, primary_key=True)),
                ('enrich_type', models.CharField(verbose_name='Enrichment type', max_length=255, blank=True, help_text='e.g. Mito, 10k')),
                ('bait_detail', models.CharField(verbose_name='Bait detail', max_length=255, blank=True, help_text='MyBait batch number')),
                ('dna_yield', models.PositiveIntegerField(blank=True, null=True)),
                ('quant_method', models.CharField(verbose_name='Quantification method', max_length=255, blank=True)),
                ('ampresult', models.ForeignKey(to='samples.AmplificationResult')),
                ('enrichment', models.ForeignKey(to='samples.Enrichment')),
            ],
        ),
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('date', models.DateField(verbose_name='Date extracted')),
                ('extracted_by', models.CharField(verbose_name='Extracted by', max_length=255)),
                ('method', models.TextField(verbose_name='Extraction method')),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtractResult',
            fields=[
                ('id', models.CharField(serialize=False, max_length=255, blank=True, primary_key=True)),
                ('starting', models.CharField(verbose_name='Starting material', max_length=255, blank=True)),
                ('final_vol', models.CharField(verbose_name='Final DNA volume', max_length=255, blank=True, help_text='(in ul)')),
                ('dna_yield', models.PositiveIntegerField(blank=True, null=True)),
                ('quant_method', models.CharField(verbose_name='Quantification method', max_length=255, blank=True, choices=[('tapestation', 'TapeStation'), ('nanodrop', 'NanoDrop'), ('qpcr', 'qPCR')])),
                ('extraction', models.ForeignKey(to='samples.Extraction')),
            ],
        ),
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to='files')),
                ('name', models.CharField(verbose_name='File name', max_length=255, blank=True)),
                ('size', models.PositiveIntegerField(verbose_name='File size', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.PositiveSmallIntegerField(verbose_name='NCBI taxonomy ID', serialize=False, primary_key=True)),
                ('genus', models.CharField(verbose_name='Genus', max_length=255, blank=True)),
                ('species', models.CharField(verbose_name='Species', max_length=255, blank=True)),
                ('subspecies', models.CharField(verbose_name='Subspecies', max_length=255, blank=True)),
                ('common', models.CharField(verbose_name='Common name', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('permit_num', models.CharField(verbose_name='Permit number', max_length=255)),
                ('valid_from', models.DateField(verbose_name='Valid from')),
                ('valid_to', models.DateField(verbose_name='Valid to')),
                ('valid_for', models.CharField(verbose_name='Valid for', max_length=255)),
                ('active_from', models.DateField(verbose_name='Active from', blank=True)),
                ('conditions', models.TextField(verbose_name='Conditions', max_length=255, blank=True)),
                ('qap', models.CharField(max_length=255, blank=True)),
                ('file', models.ManyToManyField(to='samples.FileAttachment', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Project title', max_length=255)),
                ('description', models.TextField(verbose_name='Project description', blank=True)),
                ('file', models.ManyToManyField(to='samples.FileAttachment', blank=True)),
                ('group', models.ManyToManyField(to='auth.Group', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('acad_num', models.AutoField(verbose_name='ACAD sample number', serialize=False, primary_key=True)),
                ('other_num', models.CharField(verbose_name='Other sample number', max_length=255, blank=True)),
                ('category', models.CharField(verbose_name='Category of sample', max_length=255)),
                ('extracted_by_date', models.CharField(verbose_name='Extracted by/date', max_length=255, blank=True)),
                ('acad_location', models.CharField(verbose_name='ACAD location', max_length=255, blank=True)),
                ('date_of_entry', models.DateField(verbose_name='Date of entry into ACAD', blank=True, null=True)),
                ('abc_num', models.CharField(verbose_name='ABC/Oxford sample number', max_length=255, blank=True)),
                ('common_name', models.CharField(verbose_name='Organism common name', max_length=255, blank=True)),
                ('genus', models.CharField(verbose_name='Genus', max_length=255, blank=True)),
                ('species', models.CharField(verbose_name='Species', max_length=255, blank=True)),
                ('subspecies', models.CharField(verbose_name='Subspecies', max_length=255, blank=True)),
                ('notes', models.TextField(verbose_name='Sample notes', blank=True)),
                ('region', models.CharField(verbose_name='Region', max_length=255, blank=True)),
                ('country', models.CharField(verbose_name='Country', max_length=255, blank=True)),
                ('state', models.CharField(verbose_name='State', max_length=255, blank=True)),
                ('locality', models.CharField(verbose_name='Locality', max_length=255, blank=True)),
                ('location', models.CharField(verbose_name='Specific location', max_length=255, blank=True)),
                ('lat', models.CharField(verbose_name='Latitude', max_length=255, blank=True)),
                ('lon', models.CharField(verbose_name='Longitude', max_length=255, blank=True)),
                ('datum', models.CharField(verbose_name='Map or GPS datum from which lat/lon taken', max_length=255, blank=True)),
                ('collection_date', models.DateField(verbose_name='Collection date', blank=True, null=True)),
                ('collected_by', models.CharField(verbose_name='Collected by', max_length=255, blank=True)),
                ('quality', models.CharField(verbose_name='Quality', max_length=255, blank=True)),
                ('museum', models.CharField(verbose_name='Museum name', max_length=255, blank=True)),
                ('museum_num', models.CharField(verbose_name='Museum accession number', max_length=255, blank=True)),
                ('sampled_by', models.CharField(verbose_name='Sampled by', max_length=255, blank=True)),
                ('sample_date', models.DateField(verbose_name='Date sampled', blank=True, null=True)),
                ('mismatch_reason', models.CharField(verbose_name='Mismatch reason', max_length=255, blank=True)),
                ('sample_repat', models.CharField(verbose_name='Sample repatriated', max_length=255, blank=True)),
                ('file', models.ManyToManyField(to='samples.FileAttachment', blank=True)),
                ('group', models.ForeignKey(to='samples.AQISSampleGroup', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True)),
                ('organism', models.ForeignKey(to='samples.Organism', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('path', models.TextField(verbose_name='Path to sequencing files')),
                ('amplification', models.ForeignKey(to='samples.Amplification', null=True, blank=True)),
                ('enrichment', models.ForeignKey(to='samples.Enrichment', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='sample',
            field=models.ManyToManyField(to='samples.Sample', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='extractresult',
            name='sample',
            field=models.ForeignKey(to='samples.Sample'),
        ),
        migrations.AddField(
            model_name='extraction',
            name='extract_control',
            field=models.ManyToManyField(related_name='controls', to='samples.Sample', blank=True),
        ),
        migrations.AddField(
            model_name='extraction',
            name='file',
            field=models.ManyToManyField(to='samples.FileAttachment', blank=True),
        ),
        migrations.AddField(
            model_name='enrichment',
            name='file',
            field=models.ManyToManyField(to='samples.FileAttachment', blank=True),
        ),
        migrations.AddField(
            model_name='c14',
            name='sample',
            field=models.ForeignKey(to='samples.Sample', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aqissamplegroup',
            name='permit',
            field=models.ForeignKey(to='samples.Permit', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='amplificationresult',
            name='extractresult',
            field=models.ForeignKey(to='samples.ExtractResult'),
        ),
        migrations.AddField(
            model_name='amplification',
            name='file',
            field=models.ManyToManyField(to='samples.FileAttachment', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='c14',
            unique_together=set([('centre', 'centre_num')]),
        ),
    ]
