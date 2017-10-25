
from django.core.management.base import BaseCommand
from journals.services import CoreCrawler


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--url', type=str)
        parser.add_argument('--id-inicial', type=int)
        parser.add_argument('--id-final', type=int)
        parser.add_argument('--id-journal', type=int)

    def handle(self, *args, **options):

        url = options['url']
        id_inicial = options['id_inicial']
        id_final = options['id_final']
        id_journal = options['id_journal']

        id_documents = [doc for doc in range(id_inicial, id_final)]

        crawler = CoreCrawler(url, id_journal)

        for doc in id_documents:
            fields = crawler.run(doc)
            if fields:
                self.__save_db(fields, id_journal)        
