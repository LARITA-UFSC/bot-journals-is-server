import operator

from functools import reduce
from django.core.management.base import BaseCommand
from journals.models import Documents
from django.db.models import Q


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true')
        parser.add_argument('--ingore-docs', nargs='+', type=int)

    def handle(self, *args, **options):
        save = options['save']
        ids = options.get('ingore_docs', [])

        if ids is None:
            ids = []

        expressions = [
            'Sumário',
            'Normas para publicação',
            'Notas e Registros',
            'Comunicação e Documentos',
            'Revista Completa',
            'Teses e Dissertações',
            'RESUMO DE DISSERTAÇÕES',
            'RESUMOS DE DISSERTAÇÕES',
            'Dissertações e Teses',
            'LISTA DE VALIADORES NESTE NÚMERO',
            'Editorial', 'Apresentação',
            'Expediente',
            'Prefácio',
            'Normas da Revista',
            'Normas de publicação',
            'Normas para publicação',
            'Resumos das dissertações e teses defendidas',
            'Edição completa',
            'Informação & Informação'
        ]

        filter_trash = reduce(operator.or_, (Q(title__icontains=exp) for exp in expressions))

        documents = Documents.objects.filter(filter_trash).filter(trash=False).exclude(id__in=ids)

        for document in documents:

            if save:
                document.trash = True
                document.save()

            print(document.id, document.title)
