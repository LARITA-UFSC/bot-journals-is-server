from rest_framework import serializers
from journals.models import Documents
from journals.helpers import *


class DocumentsSerializer(serializers.HyperlinkedModelSerializer):

    journal = serializers.CharField(source='journal_display')

    class Meta:
        model = Documents
        fields = ('title', 'summary', 'url_pdf', 'journal')



