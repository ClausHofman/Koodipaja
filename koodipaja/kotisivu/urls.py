from django.urls import path
from . import views

app_name = 'kotisivu'

urlpatterns = [
    path('', views.kotisivu, name='kotisivu'),
    path('site-notes/', views.kotisivu_notes, name='site-notes'),
]
