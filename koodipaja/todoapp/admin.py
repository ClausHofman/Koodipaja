from django.contrib import admin

from .models import Project, Todo, Tag

admin.site.register(Project)
admin.site.register(Todo)
admin.site.register(Tag)