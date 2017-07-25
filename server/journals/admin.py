from django.contrib import admin
from .models import Documents, Rawdata


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_filter = ['journal']
    search_fields = ['title', 'keywords', 'summary']
    readonly_fields = ['title', 'authors', 'keywords',
                       'summary', 'url_view', 'url_pdf', 'journal']


@admin.register(Rawdata)
class RawdataAdmin(admin.ModelAdmin):
    pass


admin.site.disable_action('delete_selected')