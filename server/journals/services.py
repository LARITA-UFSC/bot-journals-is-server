from bs4 import BeautifulSoup
import requests
import re
import json

from journals.helpers import Colors
from journals.models import Documents, Rawdata

class OpenJournalSystems():

    '''
    https://pkp.sfu.ca/ojs/
    '''

    def __factory_soup(self, url):
        r = requests.get(url)
        data = r.text
        return BeautifulSoup(data, 'html.parser')

    def extract(self, url):

        def filter_field(id, description, pkp):
            mt = [d['document'] for d in metadata_document if d['id'] in id and d['description'] in description and d['pkp'] in pkp]
            if len(mt) == 0:
                return ['']
            return mt

        soup_metadata = self.__factory_soup(url)
        content = soup_metadata.find('div', id='content')

        if not content:
            return None

        table = content.find('table', class_='listing')

        if not table:
            return None

        rows = table.find_all('tr', valign='top')

        if len(rows) == 0:
            return None

        metadata_document = []
        for row in rows[1:]:
            elements = row.find_all('td')
            metadata = {
                'id': elements[0].get_text().strip(),
                'description': elements[1].get_text().strip(),
                'pkp': elements[2].get_text().strip(),
                'document': elements[3].get_text().strip(),
            }

            metadata_document.append(metadata)

        title = filter_field('1.', 'Título', 'Título do documento')[0]
        authors = filter_field(
            '2.', 'Autor', 'Nome do autor, afiliação institucional, país')
        keywords = filter_field('3.', 'Assunto', 'Palavras-chave(s)')[0]
        summary = filter_field('4.', 'Descrição', 'Resumo')[0]
        url_view = filter_field('10.', 'Identificador',
                                'Identificador de Recurso Uniforme (URI)')[0]
        url_pdf = ''
        
        if url_view != '':
            soup_url_pdf = self.__factory_soup(url_view)
            div_pdf = soup_url_pdf.find('div', id='articleFullText')
            if div_pdf:
                url_pdf = div_pdf.a['href']

        fields = {
            'title': title,
            'authors': authors,
            'keywords': keywords,
            'summary': summary,
            'url_view': url_view,
            'url_pdf': url_pdf,

            'raw_data': metadata_document,
            'html_doc': soup_metadata.prettify(),
        }

        return fields


class CoreCrawler():

    def __init__(self, seed, id_journal):
        self.seed = seed
        self.id_journal = id_journal

    def run(self, document):

        ojs = OpenJournalSystems()

        subpath = f'rt/metadata/{document}'
        url = f'{self.seed}{subpath}'

        fields = ojs.extract(url)

        if fields:
            self.__save_db(fields)
        else:
            print(f'{Colors.YELLOW}Página {url} não encontrada {Colors.NO_COLOUR}')

    def __save_db(self, fields):

        doc_data = {
            'title': fields['title'],
            'authors': fields['authors'],
            'keywords': fields['keywords'],
            'summary': fields['summary'],
            'url_view': fields['url_view'],
            'url_pdf': fields['url_pdf'],
            'journal': self.id_journal,
        }
     
        document, created = Documents.objects.get_or_create(
            **doc_data,
            defaults={'url_view': doc_data['url_view'] },
        )

        if created: 
            raw_data = {
                'raw_data': json.dumps(fields['raw_data']),
                'html_doc': fields['html_doc'],
                'document': document,
            }
            Rawdata.objects.create(**raw_data,)

            print(Colors.GREEN, 'Documento ', document.id, ' processado com sucesso', Colors.NO_COLOUR)
        else:
            print(Colors.GREEN, 'Documento ', document.id, ' já foi processado', Colors.NO_COLOUR)
