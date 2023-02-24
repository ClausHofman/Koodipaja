from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('list-projects/', views.listProjects, name='list-projects'),
    path('view-single-project/<str:pk>/', views.viewSingleProject, name='view-single-project'),
    path('project-page/<str:pk>/', views.viewProjectPage, name='project-page'),
]
