from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    TFO=topicform()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=topicform(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse(str(TFD.cleaned_data))
        else:
            return HttpResponse('not valid')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=webpageform()
    d={'WFO':WFO}
    if request.method=='POST':
        WFD=webpageform(request.POST)
        if WFD.is_valid():
            WFD.save()
            return HttpResponse(str(WFD.cleaned_data))
        else:
            return HttpResponse('not valid')
    return render(request,'insert_webpage.html',d)