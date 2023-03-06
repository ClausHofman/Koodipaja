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
    list_display = ["title", "project", "created"]
    list_filter = ["project"]
    search_fields = ['title']


@admin.register(ProjectArticle)
class ProjectArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "project_page", "created"]
    list_filter = ["project", "created", "project_page"]
    search_fields = ['body', 'title']


@admin.register(ProjectPageTitle)
class ProjectPageTitleAdmin(admin.ModelAdmin):
    list_display = ["title", "project", "created"]
    # list_filter = ["project", "created", "project_page"]
    search_fields = ['body', 'title']
