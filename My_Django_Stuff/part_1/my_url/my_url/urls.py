"""my_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from my_app import views
urlpatterns = [

path('', views.index, name='index'),
path("gautam",include('my_app.urls')),
path('admin/', views.index1),

]

""" in palce of gautam we write anything when we hit http://127.0.0.1:8000/gautam
then we get Hello if we give worng path then we get 404 error

"""
