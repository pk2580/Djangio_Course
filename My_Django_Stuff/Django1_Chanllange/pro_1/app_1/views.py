from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):

    my_dict={"help_me":"My Second App of temaplates!"}
    return render(request,'help.html',context=my_dict)
