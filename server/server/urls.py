"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from journals.models import Documents
from rest_framework import routers, serializers, viewsets
from django_filters import FilterSet

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


class DocumentsFilter(FilterSet):
    class Meta:
        model = Documents
        fields = {'title': ['icontains']}


class DocumentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Documents
        fields = ('title', 'summary', 'url_pdf', 'journal_display')


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    filter_class = DocumentsFilter

router = routers.DefaultRouter()
router.register(r'documents', DocumentsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^explorer/', include('explorer.urls')),
]

urlpatterns += staticfiles_urlpatterns()
