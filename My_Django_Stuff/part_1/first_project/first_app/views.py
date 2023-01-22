from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,Accessrecord


# def index(request):
#     return HttpResponse("Hello World!")
#
# def index1(request):
#     return HttpResponse("Admin page!")

# Create your views here.

def index(request):
    # template lecture
    # my_dict={'insert_me':"Hello i am from view.py!"}
    # return render(request,'index.html',context=my_dict)

    webpage_list=Accessrecord.objects.order_by('date')
    date_dict={'access_records':webpage_list}
    return render(request,'index.html',context=date_dict)
