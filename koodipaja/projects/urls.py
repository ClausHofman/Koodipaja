from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('list-projects/', views.listProjects, name='list-projects'),
    path('view-single-project/<str:pk>/', views.viewSingleProject, name='view-single-project'),
    path('create-project/',views.createProject, name="create-project"),
    path('create-project-tag/',views.createProjectTag, name="create-project-tag"),
    path('create-project-page/<str:pk>/',views.createProjectPage, name="create-project-page"),
    path('view-project-page/<str:pk>/',views.viewProjectPage, name='view-project-page'),
    path('create-project-article/<str:pk>/',views.createProjectArticle, name='create-article'),
    path('create-project-page-tag/<str:pk>/',views.createProjectPageTag, name="create-project-page-tag"),
]
