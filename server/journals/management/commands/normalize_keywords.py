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

    def __extract_keywords(self, raw_keywords, comma, semicolon, period):
        
        keywords = self.__remove_end_stop(raw_keywords)

        sep = None

        if comma and self.__is_comma(keywords):
            sep = ','
        elif semicolon and self.__is_semicolon(keywords):
            sep = ';'
        elif period and self.__is_period(keywords):
            sep = '.'
        else:
            return None

        return list(map(str.strip, keywords.split(sep)))

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true')
        parser.add_argument('--comma', action='store_true')
        parser.add_argument('--semicolon', action='store_true')
        parser.add_argument('--period', action='store_true')

    def handle(self, *args, **options):
        
        save = options['save']

        comma = options['comma']
        semicolon = options['semicolon']
        period = options['period']

        documents=Documents.objects.filter(keywods_v1__isnull=True).filter(trash=False)
        for document in documents:

            descriptions=self.__extract_keywords(document.keywords, comma, semicolon, period)
            
            if descriptions is None:
                continue

            if save:
                for description in descriptions:
                    keyword, _=Keyword.objects.get_or_create(
                        description=description, defaults={"description": description})
                    description.keywods_v1.add(keyword)

            id_doc = document.id
            desc = ', '.join(descriptions)
            raw_desc = document.keywords

            line = f'{id_doc}|{desc}|{raw_desc}'
            print(line)
