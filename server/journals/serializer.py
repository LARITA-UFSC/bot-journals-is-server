from rest_framework import serializers
from journals.models import Documents


class DocumentsSerializer(serializers.HyperlinkedModelSerializer):

    journal = serializers.CharField(source='journal_display')
    authors = serializers.SerializerMethodField()

    def get_authors(self, obj):
        return "Foo"

    class Meta:
        model = Documents
        fields = ('title', 'summary', 'url_pdf', 'journal', 'authors')



