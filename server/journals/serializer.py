from rest_framework import serializers
from journals.models import Documents


class DocumentsSerializer(serializers.HyperlinkedModelSerializer):

    journal = serializers.CharField(source='journal_display')
    authors = serializers.SerializerMethodField()

    def get_authors(self, obj):
        authors = to_list(replace_new_line(trim_all(parenthesis_to_bracket(obj.authors))))
        return ', '.join( [a.split(';')[0] for a in authors])

    class Meta:
        model = Documents
        fields = ('title', 'summary', 'url_pdf', 'journal', 'authors')
