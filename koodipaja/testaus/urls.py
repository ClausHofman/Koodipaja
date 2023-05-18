from django.urls import path
from . import views

app_name = "testaus"

urlpatterns = [
    path('testing/', views.testingHomepage, name='testing'),

    path('testi/', views.testi_kysely, name='testi_kysely'),

    path('toggle/<int:pk>/', views.toggle_boolean, name='toggle-boolean'),

]
