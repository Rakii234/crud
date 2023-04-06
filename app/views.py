from django.shortcuts import render
from app.models import *

# Create your views here.
def tt(request):
    t=topic.objects.all()
    d={'t':t}
    return render(request,'tt.html',d)


def ww(request):
    w=webpage.objects.all()
    k={'w':w}
    return render(request,'ww.html',k)