# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Keyword(models.Model):
    description = models.CharField(max_length=150, blank=False, null=False, unique=True)

    def __str__(self):
        return self.description


class Author(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class AuthorMember(models.Model):
    author = models.ForeignKey('Author')
    documents = models.ForeignKey('Documents')
    order = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return f'{self.order} - {self.author} - {self.documents}'


class Documents(models.Model):

    DEFAULT = 0
    INFORMACAO_E_SOCIEDADE = 1
    TRANSINFORMACAO = 2
    PERSPECTIVAS_EM_CIENCIAS_DA_INFORMACAO = 3
    INFORMACAO_E_INFORMACAO = 4
    EM_QUESTAO = 5
    AGORA = 6
    INCID = 7
    INTEXTO = 8
    TENDENCIAS_DA_PESQUISA_BRASILEIRA_EM_CI = 9
    RBBD = 10
    BRAZILIAN_JOURNAL_OF_INFORMATION_SCIENCE = 11
    PONTO_DE_ACESSO = 12
    RIACI = 13
    RACB = 14
    BIBLIOS = 15
    CIENCIA_DA_INFORMACAO_EM_REVISTA = 16
    REVISTA_CONHECIMENTO_EM_ACAO = 17
    FOLHA_DE_ROSTO = 18
    MULTIPLOS_OLHARES_EM_CIENCIAS_DA_INFORMACAO = 19
    REVISTA_ELETRONICA_DE_COMUNICACAO_INFORMACAO_INIVACAO_EM_SAUDE = 20

    JOURNALS_CHOICES = (
        (DEFAULT, 'Não Informado'),
        (INFORMACAO_E_SOCIEDADE, 'Informação & Sociedade'),
        (TRANSINFORMACAO, 'Transinformação'),
        (PERSPECTIVAS_EM_CIENCIAS_DA_INFORMACAO, 'Perspectivas em Ciência da Informação'),
        (INFORMACAO_E_INFORMACAO, 'Informação & Informação'),
        (EM_QUESTAO, 'Em Questão'),
        (AGORA, 'Ágora'),
        (INCID, 'InCID: Revista de Ciência da Informação e Documentação'),
        (INTEXTO, 'Intexto'),
        (TENDENCIAS_DA_PESQUISA_BRASILEIRA_EM_CI,
         'Tendências da Pesquisa Brasileira em Ciência da Informação'),
        (RBBD, 'Revista Brasileira de Biblioteconomia e Documentação'),
        (BRAZILIAN_JOURNAL_OF_INFORMATION_SCIENCE,
         'BRAZILIAN JOURNAL OF INFORMATION SCIENCE: RESEARCH TRENDS'),
        (PONTO_DE_ACESSO, 'Ponto de Acesso'),
        (RIACI, 'Revista Ibero-Americana de Ciência da Informação'),
        (RACB, 'Revista ACB'),
        (BIBLIOS, 'Biblios'),
        (CIENCIA_DA_INFORMACAO_EM_REVISTA, 'Ciência da Informação em Revista'),
        (REVISTA_CONHECIMENTO_EM_ACAO, 'Revista Conhecimento em Ação'),
        (FOLHA_DE_ROSTO, 'Folha de Rosto'),
        (MULTIPLOS_OLHARES_EM_CIENCIAS_DA_INFORMACAO, 'Múltiplos Olhares em Ciência da Informação'),
        (REVISTA_ELETRONICA_DE_COMUNICACAO_INFORMACAO_INIVACAO_EM_SAUDE,
         'Revista Eletrônica de Comunicação, Informação & Inovação em Saúde'),
    )

    title = models.CharField(max_length=2000, blank=True, null=True)
    authors = models.CharField(max_length=2000, blank=True, null=True)
    keywords = models.CharField(max_length=2000, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    url_view = models.CharField(max_length=2000, blank=True, null=True, unique=True)
    url_pdf = models.CharField(max_length=2000, blank=True, null=True)

    authors_v3 = models.ManyToManyField(Author, through='AuthorMember', default=None)
    keywods_v1 = models.ManyToManyField(Keyword, default=None)

    trash = models.BooleanField(default=False)

    journal = models.PositiveSmallIntegerField(
        choices=JOURNALS_CHOICES,
        default=DEFAULT,
    )

    @property
    def journal_display(self):
        return self.get_journal_display()

    class Meta:
        # managed = False
        db_table = 'documents'
        ordering = ['title']

    def __str__(self):
        return self.title


class Rawdata(models.Model):
    raw_data = models.TextField(blank=True, null=True)
    html_doc = models.TextField(blank=True, null=True)
    document = models.ForeignKey(Documents, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawdata'
