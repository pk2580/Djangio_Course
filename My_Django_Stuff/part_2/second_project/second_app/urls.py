from django.urls import include, path
from second_app import views

urlpatterns=[
path('',views.index,name='index'),
]
