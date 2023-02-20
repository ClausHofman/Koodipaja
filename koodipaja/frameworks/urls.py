from django.urls import path

from . import views

app_name = "frameworks"

urlpatterns = [
    path('framework/<str:pk>/', views.viewSingleFramework, name='view-framework'),
    path('framework-example/<str:pk>/', views.viewSingleExample, name='view-example'),
    path('framework-list/', views.listFrameworks, name='framework-list'),
]