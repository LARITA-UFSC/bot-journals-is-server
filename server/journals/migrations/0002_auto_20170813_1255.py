# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='journal',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Não Informado'), (1, 'Informação & Sociedade'), (2, 'Transinformação'), (3, 'Perspectivas em Ciência da Informação'), (4, 'Informação & Informação'), (5, 'Em Questão')], default=0),
        ),
    ]
