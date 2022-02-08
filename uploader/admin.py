from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('description', 'uploaded_at')


# Register your models here.
admin.site.register(Document, DocumentAdmin)

