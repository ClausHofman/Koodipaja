from datetime import date
from django.contrib import admin
from .models import (Project, ProjectPage, ProjectArticle, ProjectTag, ProjectPageTag, ProjectArticleTag,
                     ProjectTodo, ProjectTodoTag, ProjectPageTitle)

# Register your models here.
admin.site.register(Project)
# admin.site.register(ProjectTodo)
admin.site.register(ProjectTag)
# admin.site.register(ProjectTodoTag)
admin.site.register(ProjectPageTag)
# admin.site.register(ProjectPageTitle)
admin.site.register(ProjectArticleTag)


@admin.register(ProjectPage)
class ProjectPageAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "project"]
    list_filter = ["project", "created"]
    search_fields = ['title']


@admin.register(ProjectArticle)
class ProjectArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "project_page"]

    # Option to filter articles in the django admin panel
    list_filter = ["project", "created", "project_page"]

    # Related lookup
    # search_fields = ['foreign_key__related_fieldname']
    search_fields = ['body', 'project__title']

    # ModelAdmin.raw_id_fields
    # The raw_id_fields widget shows a magnifying glass button next to the field which allows
    # users to search for and select a value. (in the django admin panel)
    raw_id_fields = ["project_page", "article_title"]


@admin.register(ProjectPageTitle)
class ProjectPageTitleAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "project"]
    list_filter = ["project"]
    search_fields = ['body', 'title']
