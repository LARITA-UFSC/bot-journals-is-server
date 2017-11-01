from django.db.models import Q
from django_filters import FilterSet, CharFilter
from journals.models import Documents


class DocumentsFilter(FilterSet):

    search = CharFilter(name='search', method='filter_search')

    def filter_search(self, queryset, name, value):
        query = Q(authors__icontains=value) | Q(title__icontains=value) | Q(
            keywords__icontains=value) | Q(summary__icontains=value) | Q(journal__description__icontains=value)

        return queryset.filter(query)

    class Meta:
        model = Documents
        fields = ['search']
