from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('account/', views.userAccount, name="account"),
    path('favorite-articles/', views.show_favorite_articles,
         name="favorite-articles"),
]
