from django.shortcuts import render

from .models import Turi,Gul

def asosiy(request):
    turlar = Turi.objects.all()
    gullar = Gul.objects.all()
    contects = {
        'turlar' : turlar,
        'gullar' : gullar,
    }
    return render(request, 'index.html', context= contects)

def gul_tur(request, tur_id):
    turlar = Turi.objects.all()
    gullar = Gul.objects.objects.filter(tur = tur_id)

    contexts = {
        'turlar' : turlar,
        'gullar' : gullar,
    }
    return render(request, "index.html", context = contexts)

def gul(request, gul_id):
    turlar = Turi.objects.all()
    gullar = Gul.objects.objects.filter(gul =gul_id)
    contexts = {
        'turlar' : turlar,
        'gullar' : gullar,
    }
    return render(request, "index.html", context = contexts)


