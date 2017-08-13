# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Documents(models.Model):

    DEFAULT = 0
    INFORMACAO_E_SOCIEDADE = 1
    TRANSINFORMACAO = 2
    PERSPECTIVAS_EM_CIENCIAS_DA_INFORMACAO = 3
    INFORMACAO_E_INFORMACAO = 4
    EM_QUESTAO = 5
    
    JOURNALS_CHOICES = (
        (DEFAULT, 'Não Informado'),
        (INFORMACAO_E_SOCIEDADE, 'Informação & Sociedade'),
        (TRANSINFORMACAO, 'Transinformação'),
        (PERSPECTIVAS_EM_CIENCIAS_DA_INFORMACAO, 'Perspectivas em Ciência da Informação'),
        (INFORMACAO_E_INFORMACAO, 'Informação & Informação'),
        (EM_QUESTAO, 'Em Questão'),
    )

    title = models.CharField(max_length=2000, blank=True, null=True)
    authors = models.CharField(max_length=2000, blank=True, null=True)
    keywords = models.CharField(max_length=2000, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    url_view = models.CharField(max_length=2000, blank=True, null=True)
    url_pdf = models.CharField(max_length=2000, blank=True, null=True)
    
    journal = models.PositiveSmallIntegerField(
        choices=JOURNALS_CHOICES,
        default=DEFAULT,
    )

    class Meta:
        # managed = False
        db_table = 'documents'

    def __str__(self):
        return self.title


class Rawdata(models.Model):
    raw_data = models.TextField(blank=True, null=True)
    html_doc = models.TextField(blank=True, null=True)
    document = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawdata'
