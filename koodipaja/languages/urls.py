from django.urls import path

from . import views

app_name = "languages"

urlpatterns = [
    path('view-language/<str:pk>/', views.viewSingleLanguage, name='view-language'),
    path('language-example/<str:pk>/', views.viewSingleExample, name='view-example'),
    path('list-languages/', views.listLanguages, name='list-languages'),
    path('new-example/<str:pk>/',views.createLanguageExample, name="new-example"),
]