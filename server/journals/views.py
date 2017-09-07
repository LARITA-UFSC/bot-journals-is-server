from rest_framework import viewsets
from journals.serializer import DocumentsSerializer
from journals.filters import DocumentsFilter
from journals.models import Documents


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    filter_class = DocumentsFilter