from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def index1(request):
    return HttpResponse("Admin page!")

# Create your views here.
