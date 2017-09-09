from django.core.management.base import BaseCommand
from journals.models import Documents, Keyword


class Command(BaseCommand):

    def __remove_end_stop(self, text):
        if text.endswith('.'):
            return text[:-1]
        return text

    def __is_comma(self, text):
        return text.count(',') > 0

    def __is_semicolon(self, text):
        return text.count(';') > 0

    def __is_period(self, text):
        return text.count('.') > 0

    def __extract_keywords(self, raw_keywords):

        keywords = self.__remove_end_stop(raw_keywords)

        sep = None

        if self.__is_comma(keywords):
            sep = ','
        elif self.__is_semicolon(keywords):
            sep = ';'
        elif self.__is_period(keywords):
            sep = '.'
        # else:
        #     raise Exception(f'Separador não identificado - {keywords}')

        return list(map(str.strip, keywords.split(sep)))

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true')

    def handle(self, *args, **options):
        save=options['save']

        documents=Documents.objects.filter(keywods_v1__isnull=True).filter(trash=False)
        for document in documents:
            descriptions=self.__extract_keywords(document.keywords)
            
            if save:
                for description in descriptions:
                    keyword, _=Keyword.objects.get_or_create(
                        description=description, defaults={"description": description})
                    description.keywods_v1.add(keyword)

            print(document.id, descriptions)
