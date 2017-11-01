from django.db import migrations
from journals.helpers import *


def popule_journal(apps, schema_editor):

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

    Journal = apps.get_model('journals', 'Journal')

    journals = [ Journal(id=id, description=description) for (id, description) in JOURNALS_CHOICES ]
    
    Journal.objects.bulk_create(journals)


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0012_journal'),
    ]

    operations = [
        migrations.RunPython(popule_journal, reverse_code=migrations.RunPython.noop),
    ]