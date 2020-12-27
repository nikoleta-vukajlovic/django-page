from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('home', views.home, name="home"),
    path('login_as', views.login_as, name="login_as"),
    path('logout', views.logout, name="logout")
]