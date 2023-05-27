from django.shortcuts import render
from .models import Zametka

# Create your views here.

def index(request):
    zametki = Zametka.objects.order_by('-date_added')
    context = {
        "zametki" : zametki,
    }
    return  render(request,'index.html',context)

def zametka(request,zametka_id):
    zametka = Zametka.objects.get(id=zametka_id)
    podrobnosti = zametka.entry_set.order_by('-date_added')
    context = {
        "zametka" : zametka,
        "podrobnosti": podrobnosti,
    }
    return render(request,'zametka.html',context)





















