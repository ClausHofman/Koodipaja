from django.urls import path

from . import views

app_name = "languages"

urlpatterns = [
    path('list/', views.listLanguages, name="language-list"),
    path('language/<str:pk>/', views.viewSingleLanguage, name='view-language'),
    path('list-examples/', views.listExamples, name='language-examples'),
]