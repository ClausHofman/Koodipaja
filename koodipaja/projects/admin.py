from django.contrib import admin
from .models import (Project, ProjectPage, ProjectArticle, ProjectTag, ProjectPageTag, ProjectArticleTag,
                    ProjectTodo, ProjectTodoTag)

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectTodo)
admin.site.register(ProjectPage)
admin.site.register(ProjectArticle)
admin.site.register(ProjectTag)
admin.site.register(ProjectTodoTag)
admin.site.register(ProjectPageTag)
admin.site.register(ProjectArticleTag)