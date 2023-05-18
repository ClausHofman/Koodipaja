from django.urls import path
from . import views

app_name = "testaus"

urlpatterns = [
    path('testing/', views.testingHomepage, name='testing'),
    path('viewtest1/<str:pk>/', views.viewTest1, name='viewtest1'),
    path('viewtest2/<str:pk>/', views.viewTest2, name='viewtest2'),

    path('toggle/<int:pk>/', views.toggle_boolean, name='toggle-boolean'),

]
