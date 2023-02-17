from django.urls import path

from . import views

app_name = "tktutkija"

urlpatterns = [
    path('tkt/', views.tktIndex, name='tkt'),
    path('kysely1/', views.kysely1, name='kysely1'),
    path('kysely2/', views.kysely2, name='kysely2'),

    path('kysely1/<str:pk>/', views.kysely3, name='kysely3'),
]