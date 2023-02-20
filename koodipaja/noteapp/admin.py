from django.contrib import admin

from .models import GeneralNote, Tag

admin.site.register(GeneralNote)
admin.site.register(Tag)