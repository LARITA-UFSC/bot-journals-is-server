from django.contrib import admin
from .models import Documents, Rawdata


@admin.register(CustomPropertiesMixinAdmin, Documents)
class DocumentsAdmin(admin.ModelAdmin, CustomPropertiesMixinAdmin):
    list_filter = ['journal']
    search_fields = ['title', 'keywords', 'summary']
    readonly_fields = ['title', 'authors', 'keywords',
                       'summary', 'url_view', 'url_pdf', 'journal']


@admin.register(CustomPropertiesMixinAdmin, Rawdata)
class RawdataAdmin(admin.ModelAdmin, CustomPropertiesMixinAdmin):
    pass
