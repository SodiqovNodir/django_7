from lib2to3.fixes.fix_input import context

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TurForm, GulForm
from .models import Turi,Gul

def asosiy(request):
    turlar = Turi.objects.all()
    turar = Gul.objects.all()
    contects = {
        'turlar' : turlar,
        'turar' : turar,
    }
    return render(request, 'index.html', context= contects)

def gul_tur(request, turi_id):
    turlar = Turi.objects.all()
    turar = Gul.objects.objects.filter(turi_id=turi_id)

    contexts = {
        'turlar' : turlar,
        'turar' : turar,
    }
    return render(request, "index.html", context = contexts)

def gul(request, gul_id):
    turlar = Turi.objects.all()
    turar = Gul.objects.objects.filter(gul_id=gul_id)
    contexts = {
        'turlar' : turlar,
        'turar' : turar,
    }
    return render(request, "index.html", context = contexts)

def batafsil(request, gul_id):
    turar = Gul.objects.get(id = gul_id)
    contexts = {
        'turar': turar,
    }

    return render(request, 'batafsil.html', context=contexts)



def add_tur(request: WSGIRequest):

    if request.method == 'POST':
        tur = TurForm(data=request.POST, files=request.FILES)
        if tur.is_valid():
            turlar = Turi.objects.create(**tur.cleaned_data)
            return redirect('home', turlar)
    turla = TurForm()
    contexts = {
        'turla' : turla,
    }
    return render(request, 'add_tur.html', context = contexts)

def add_gul(request: WSGIRequest):
    if request.method == 'POST':
        lesson = GulForm(data=request.POST, files=request.FILES)
        if lesson.is_valid():
            turar = Gul.objects.create(**gul.cleaned_data)
            return redirect('home', turar)

    turar = GulForm
    contexts = {
        'turar' : turar,
    }
    return render(request, 'add_gul.html', context = contexts)

def update_gul(request:WSGIRequest, gul_id):
    tur = get_object_or_404(Gul, pk = gul_id)

    if request.method == 'POST':
        form = GulForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            tur.nomi = form.cleaned_data.get('nomi')
            tur.malumot = form.cleaned_data.get('malumot')
            tur.rasm = form.cleaned_data.get('rasm') if form.cleaned_data.get('rasm') else tur.rasm
            tur.created = form.cleaned_data.get('created')
            tur.turi = form.cleaned_data.get('turi')
            tur.save()


    form = GulForm(initial={
        'nomi': tur.nomi,
        'rasm': tur.rasm,
        'malumot':tur.malumot,
        'created': tur.created,
        'turi': tur.turi
    })

    contexts = {
        'form' : form,
        'photo':tur.rasm
    }
    return render(request, 'add_gul.html', context = contexts)


def update_tur(request:WSGIRequest, turi_id):
    tur = get_object_or_404(Turi, pk = turi_id)

    if request.method == 'POST':
        form = TurForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            tur.nomi = form.cleaned_data.get('nomi')
            tur.malumot = form.cleaned_data.get('malumot')
            tur.rasm = form.cleaned_data.get('rasm') if form.cleaned_data.get('rasm') else tur.rasm
            tur.created = form.cleaned_data.get('created')
            tur.save()


    form = GulForm(initial={
        'nomi': tur.nomi,
        'rasm': tur.rasm,
        'malumot':tur.malumot,
        'created': tur.created,
        'turi': tur.turi
    })

    contexts = {
        'form' : form,
        'photo':tur.rasm
    }
    return render(request, 'add_gul.html', context = contexts)
