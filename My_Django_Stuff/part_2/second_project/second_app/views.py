from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={'insert_content':"Now I am Visible ot you!"}
    return render(request,'app/index.html',context=my_dict)
