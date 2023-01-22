from django.urls import include, path
from my_app import views

urlpatterns=[
path('',views.index,name='index'),
]
