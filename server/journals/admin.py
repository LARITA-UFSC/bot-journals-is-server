from django.contrib import admin
from .models import Documents, Rawdata


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Rawdata)
class RawdataAdmin(admin.ModelAdmin):
    pass
