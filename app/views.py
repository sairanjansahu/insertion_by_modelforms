from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TO=Topicform()
    d={'TO':TO}
    if request.method=='POST':
        TOD=Topicform(request.POST)
        if TOD.is_valid():
            TOD.save()
            return HttpResponse('insertion done succesfully')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WO=Webpageform()
    d={'WO':WO}
    if request.method=='POST':
        WOD=Webpageform(request.POST)
        if WOD.is_valid():
            WOD.save()
            return HttpResponse('insertion done succesfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    AO=AccesRecordform()
    d={'AO':AO}
    if request.method=='POST':
        AOD=AccesRecordform(request.POST)
        if AOD.is_valid():
            AOD.save()
            return HttpResponse('insertion done succesfully')
    return render(request,'insert_accessrecord.html',d)