from django.contrib import admin
from .models import Language, LanguageExample, Tag
# Register your models here.

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["language_name", "owner", "created"]

@admin.register(LanguageExample)
class LanguageExampleAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    search_fields = ['description']
    class Meta:
        list_filter = ['-created']

admin.site.register(Tag)