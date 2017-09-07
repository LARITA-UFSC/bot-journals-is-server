from django.db import migrations
from journals.helpers import *


def split_authors(apps, schema_editor):
    Documents = apps.get_model('journals', 'Documents')
    Author = apps.get_model('journals', 'Author')
    AuthorMember = apps.get_model('journals', 'AuthorMember')

    for document in Documents.objects.exclude(title__exact=''):

        authors = document.authors
        autores = to_list(replace_new_line(trim_all(parenthesis_to_bracket(authors))))

        for index, autor in enumerate(autores):
            name = autor.split(';')[0]

            aut, _ = Author.objects.get_or_create(name=name, defaults={"name": name})
            autor_member = AuthorMember.objects.create(author=aut, documents=document, order=index + 1)
            print(document.id, name)


def reverte_split_authors(apps, schema_editor):
    Author = apps.get_model('journals', 'Author')
    AuthorMember = apps.get_model('journals', 'AuthorMember')

    Author.objects.all().delete()
    AuthorMember.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0006_auto_20170907_1708'),
    ]

    operations = [
        migrations.RunPython(split_authors, reverse_code=reverte_split_authors),
    ]