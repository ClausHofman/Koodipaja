from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path('', views.projectIndex, name='projects'),
]