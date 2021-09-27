from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name="loginpage"),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('paid_time_off', views.paid_time_off, name='paid_time_off'),

   
]