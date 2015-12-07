# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amplification',
            name='amp_type',
            field=models.CharField(verbose_name='Amplification type', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='amplification',
            name='prepared_by',
            field=models.CharField(verbose_name='Prepared by', max_length=2048),
        ),
        migrations.AlterField(
            model_name='amplification',
            name='treatment',
            field=models.CharField(verbose_name='Treatment', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='amplificationresult',
            name='id',
            field=models.CharField(serialize=False, blank=True, max_length=2048, primary_key=True),
        ),
        migrations.AlterField(
            model_name='amplificationresult',
            name='quant_method',
            field=models.CharField(verbose_name='Quantification method', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='acad_loc',
            field=models.CharField(verbose_name='ACAD location', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='aqis_num',
            field=models.CharField(verbose_name='AQIS Quarantine Entry/Order Number', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='contact',
            field=models.CharField(verbose_name='ACAD contact', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='description',
            field=models.CharField(verbose_name='Goods description', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='group_num',
            field=models.CharField(serialize=False, verbose_name='Group number', max_length=2048, blank=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='movement',
            field=models.CharField(verbose_name='Movement and transfer', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='notes',
            field=models.CharField(verbose_name='Other relevant info', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='origin',
            field=models.CharField(verbose_name='Country of origin', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='permit_num',
            field=models.CharField(verbose_name='Permit number', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='aqissamplegroup',
            name='sent_by',
            field=models.CharField(verbose_name='Sent by', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='c14',
            name='centre',
            field=models.CharField(verbose_name='Centre that did carbon dating', max_length=2048),
        ),
        migrations.AlterField(
            model_name='c14',
            name='centre_num',
            field=models.CharField(verbose_name='Centre reference number', max_length=2048),
        ),
        migrations.AlterField(
            model_name='c14',
            name='date',
            field=models.CharField(verbose_name='Estimated age in radiocarbon years', max_length=2048),
        ),
        migrations.AlterField(
            model_name='c14',
            name='sampref',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='c14',
            name='slug',
            field=models.SlugField(null=True, blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='enrichment',
            name='prepared_by',
            field=models.CharField(verbose_name='Prepared by', max_length=2048),
        ),
        migrations.AlterField(
            model_name='enrichmentresult',
            name='bait_detail',
            field=models.CharField(help_text='MyBait batch number', verbose_name='Bait detail', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='enrichmentresult',
            name='enrich_type',
            field=models.CharField(help_text='e.g. Mito, 10k', verbose_name='Enrichment type', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='enrichmentresult',
            name='id',
            field=models.CharField(serialize=False, blank=True, max_length=2048, primary_key=True),
        ),
        migrations.AlterField(
            model_name='enrichmentresult',
            name='quant_method',
            field=models.CharField(verbose_name='Quantification method', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='extraction',
            name='extracted_by',
            field=models.CharField(verbose_name='Extracted by', max_length=2048),
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='final_vol',
            field=models.CharField(help_text='(in ul)', verbose_name='Final DNA volume', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='id',
            field=models.CharField(serialize=False, blank=True, max_length=2048, primary_key=True),
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='quant_method',
            field=models.CharField(choices=[('tapestation', 'TapeStation'), ('nanodrop', 'NanoDrop'), ('qpcr', 'qPCR')], verbose_name='Quantification method', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='extractresult',
            name='starting',
            field=models.CharField(verbose_name='Starting material', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='name',
            field=models.CharField(verbose_name='File name', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='organism',
            name='common',
            field=models.CharField(verbose_name='Common name', max_length=2048),
        ),
        migrations.AlterField(
            model_name='organism',
            name='genus',
            field=models.CharField(verbose_name='Genus', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='organism',
            name='species',
            field=models.CharField(verbose_name='Species', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='organism',
            name='subspecies',
            field=models.CharField(verbose_name='Subspecies', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='conditions',
            field=models.TextField(verbose_name='Conditions', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='permit_num',
            field=models.CharField(verbose_name='Permit number', max_length=2048),
        ),
        migrations.AlterField(
            model_name='permit',
            name='qap',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AlterField(
            model_name='permit',
            name='valid_for',
            field=models.CharField(verbose_name='Valid for', max_length=2048),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(verbose_name='Project title', max_length=2048),
        ),
        migrations.AlterField(
            model_name='sample',
            name='abc_num',
            field=models.CharField(verbose_name='ABC/Oxford sample number', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='acad_location',
            field=models.CharField(verbose_name='ACAD location', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='category',
            field=models.CharField(verbose_name='Category of sample', max_length=2048),
        ),
        migrations.AlterField(
            model_name='sample',
            name='collected_by',
            field=models.CharField(verbose_name='Collected by', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='common_name',
            field=models.CharField(verbose_name='Organism common name', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='country',
            field=models.CharField(verbose_name='Country', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='datum',
            field=models.CharField(verbose_name='Map or GPS datum from which lat/lon taken', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='extracted_by_date',
            field=models.CharField(verbose_name='Extracted by/date', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='genus',
            field=models.CharField(verbose_name='Genus', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='lat',
            field=models.CharField(verbose_name='Latitude', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='locality',
            field=models.CharField(verbose_name='Locality', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='location',
            field=models.CharField(verbose_name='Specific location', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='lon',
            field=models.CharField(verbose_name='Longitude', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='mismatch_reason',
            field=models.CharField(verbose_name='Mismatch reason', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='museum',
            field=models.CharField(verbose_name='Museum name', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='museum_num',
            field=models.CharField(verbose_name='Museum accession number', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='other_num',
            field=models.CharField(verbose_name='Other sample number', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='quality',
            field=models.CharField(verbose_name='Quality', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='region',
            field=models.CharField(verbose_name='Region', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sample_repat',
            field=models.CharField(verbose_name='Sample repatriated', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='sampled_by',
            field=models.CharField(verbose_name='Sampled by', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='species',
            field=models.CharField(verbose_name='Species', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='state',
            field=models.CharField(verbose_name='State', max_length=2048, blank=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='subspecies',
            field=models.CharField(verbose_name='Subspecies', max_length=2048, blank=True),
        ),
    ]
