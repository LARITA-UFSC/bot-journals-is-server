import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

import django
django.setup()


def main():
    from django.conf import settings
    from journals.models import Documents

    print(Documents.objects.all().count())

if __name__ == '__main__':
    main()
