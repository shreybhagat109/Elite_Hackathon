"""employeesystem URL Configuration

The `urlpatterns` list routes URLs to s. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function s
    1. Add an import:  from my_app import s
    2. Add a URL to urlpatterns:  path('', s.home, name='home')
Class-based s
    1. Add an import:  from other_app.s import Home
    2. Add a URL to urlpatterns:  path('', Home.as_(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("work.urls")),
   
]
