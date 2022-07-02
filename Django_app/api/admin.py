from django.contrib import admin
from api.models import *

# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'comments', 'date_add']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name_lang']