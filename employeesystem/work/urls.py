from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path("loginpage", views.loginpage, name="loginpage"),
    path("register", views.register, name="register")
   
]