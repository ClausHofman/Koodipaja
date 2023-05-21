from django.urls import path
from . import views

app_name = "testaus"

urlpatterns = [
    path('testing/', views.testingHomepage, name='testing'),

    path('testi/', views.testi_kysely, name='testi_kysely'),

    path('toggle/<int:pk>/', views.toggle_boolean, name='toggle-boolean'),

    path('muistipeli/', views.muistipeli, name='muistipeli'),

    path('create-malli-1/', views.create_malli1, name='create-malli-1'),
    path('new-muistipeli/', views.new_muistipeli, name='new-muistipeli'),
    path('move_game/', views.move_game, name='move-game'),

    path('send_dict/', views.send_dictionary, name='send-dict'),

]
