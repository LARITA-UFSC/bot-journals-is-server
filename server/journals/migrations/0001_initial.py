# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=2000, null=True)),
                ('authors', models.CharField(blank=True, max_length=2000, null=True)),
                ('keywords', models.CharField(blank=True, max_length=2000, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('url_view', models.CharField(blank=True, max_length=2000, null=True)),
                ('url_pdf', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'documents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rawdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.TextField(blank=True, null=True)),
                ('html_doc', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rawdata',
                'managed': False,
            },
        ),
    ]
