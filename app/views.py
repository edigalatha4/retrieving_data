from django.shortcuts import render
from app.models  import *

# Create your views here.
def display_topic(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSW=Webpage.objects.all()
    d={'webpages':QSW}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    QSA=AccessRecord.objects.all()
    d={'accessrecord':QSA}

    return render(request,'display_accessrecord.html',d)