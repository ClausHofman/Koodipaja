from django.urls import path
from . import views
from .views import cards_test_page, get_data

app_name = "testaus"

urlpatterns = [
    path('cards_test_page/', cards_test_page, name='cards_test_page'),
    path('get_data/', get_data, name='get_data'),


    path('testing/', views.testingHomepage, name='testing'),

    path('general/', views.general_testing, name='general-testing'),

    path('testi/', views.testi_kysely, name='testi_kysely'),

    path('toggle/<int:pk>/', views.toggle_boolean, name='toggle-boolean'),

    path('muistipeli/', views.muistipeli, name='muistipeli'),

    path('create-malli-1/', views.create_malli1, name='create-malli-1'),
    path('new-muistipeli/', views.new_muistipeli, name='new-muistipeli'),
    path('move-active/<int:pk>/',
         views.move_question_to_active, name='move-question-to-active'),
    path('move-inactive/<int:pk>/',
         views.move_question_to_inactive, name='move-question-to-inactive'),

    path('send_dict/', views.send_dictionary, name='send-dict'),
    
]
