from django.urls import path, include
from . import views

urlpatterns = [
    
    path('list-projects/', views.listProjects, name='list-projects'),
    path('list-project-pages/<str:pk>/',
         views.viewSingleProject, name='list-project-pages'),
    path('create-project/', views.createProject, name="create-project"),
    path('create-project-tag/', views.createProjectTag, name="create-project-tag"),
    path('create-project-page/<str:pk>/',
         views.createProjectPage, name="create-project-page"),
    path('list-page-titles/<str:pk>/',
         views.viewProjectPage, name='list-page-titles'),
    path('list-page-articles/<str:pk>/',
         views.viewPageTitle, name='list-page-articles'),
    path('create-project-article/<str:pk>/',
         views.createProjectArticle, name='create-article'),
    path('update-article/<str:pk>/', views.updateArticle, name='update-article'),
    path('create-project-page-tag/<str:pk>/',
         views.createProjectPageTag, name="create-project-page-tag"),
    path('create-project-page-title/<str:pk>/',
         views.createProjectPageTitle, name='create-project-page-title'),
    path('view-article-title/<str:pk>/',
         views.viewArticleTitle, name='view-article-title'),
    path('search-page-titles/', views.search_titles, name='search-page-titles'),
    path('search-article-titles/', views.search_articles,
         name='search-article-titles'),
]

app_name = 'projects'
