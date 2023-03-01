from datetime import date
from django.contrib import admin
from .models import (Project, ProjectPage, ProjectArticle, ProjectTag, ProjectPageTag, ProjectArticleTag,
                     ProjectTodo, ProjectTodoTag)

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTodo)
admin.site.register(ProjectPage)
admin.site.register(ProjectTag)
admin.site.register(ProjectTodoTag)
admin.site.register(ProjectPageTag)
admin.site.register(ProjectArticleTag)


@admin.register(ProjectArticle)
class ProjectArticleAdmin(admin.ModelAdmin):
    list_display = ["created", "project_page", "title"]
    search_fields = ['body']

    class Meta:
        list_filter = ["-created"]
