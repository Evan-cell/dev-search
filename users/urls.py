from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>', views.userprofile, name="userprofile"),
]