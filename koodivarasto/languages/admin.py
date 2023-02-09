from django.contrib import admin
from .models import Language
# Register your models here.

@admin.register(Language)
class Project(admin.ModelAdmin):
    list_display = ["language_name", "owner", "language_created"]