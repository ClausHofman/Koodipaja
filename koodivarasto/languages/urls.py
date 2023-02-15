from django.urls import path

from . import views

app_name = "languages"

urlpatterns = [
    path('language/<str:pk>/', views.viewSingleLanguage, name='view-language'),
    path('list-examples/', views.listExamples, name='language-examples'),
    path('list/', views.listLanguages, name='language-list'),
]