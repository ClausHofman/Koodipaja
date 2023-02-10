from django.contrib import admin
from .models import Language, LanguageExample
# Register your models here.

@admin.register(Language)
class Project(admin.ModelAdmin):
    list_display = ["language_name", "owner", "language_created"]

@admin.register(LanguageExample)
class LanguageExampleAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    search_fields = ['description']
    class Meta:
        list_filter = ['-created']