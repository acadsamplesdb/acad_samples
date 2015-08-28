# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0003_auto_20150707_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file', models.FileField(upload_to='files')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='group',
            field=models.ManyToManyField(to='auth.Group', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='sample',
            field=models.ManyToManyField(to='samples.Sample', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='file',
            field=models.ManyToManyField(to='samples.FileAttachment', blank=True),
        ),
    ]
