from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from .forms import TurForm, GulForm
from .models import Turi,Gul

def asosiy(request):
    turlar = Turi.objects.all()
    gullar = Gul.objects.all()
    contects = {
        'turlar' : turlar,
        'gullar' : gullar,
    }
    return render(request, 'index.html', context= contects)

def gul_tur(request, turi_id):
    turlar = Turi.objects.all()
    gullar = Gul.objects.objects.filter(turi_id=turi_id)

    contexts = {
        'turlar' : turlar,
        'gullar' : gullar,
    }
    return render(request, "index.html", context = contexts)

def gul(request, gul_id):
    turlar = Turi.objects.all()
    gullar = Gul.objects.objects.filter(gul_id=gul_id)
    contexts = {
        'turlar' : turlar,
        'gullar' : gullar,
    }
    return render(request, "index.html", context = contexts)



def add_tur(request: WSGIRequest):

    if request.method == 'POST':
        tur = TurForm(data=request.POST, files=request.FILES)
        if tur.is_valid():
            Turi.objects.create(**tur.cleaned_data)

    turla = TurForm()
    contexts = {
        'turla' : turla,
    }
    return render(request, 'add_tur.html', context = contexts)

def add_gul(request: WSGIRequest):
    if request.method == 'POST':
        lesson = GulForm(data=request.POST, files=request.FILES)
        if lesson.is_valid():
            Gul.objects.create(**gul.cleaned_data)

    gullar = GulForm
    contexts = {
        'gullar' : gullar,
    }
    return render(request, 'add_gul.html', context = contexts)