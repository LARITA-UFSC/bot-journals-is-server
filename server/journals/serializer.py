from rest_framework import serializers
from journals.models import Documents


class DocumentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Documents
        fields = ('title', 'summary', 'url_pdf', 'journal_display')



