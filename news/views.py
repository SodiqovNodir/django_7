from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import TurForm, GulForm, RegisterForm, LoginForm
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

def batafsil(request, gul_id):
    gullar = Gul.objects.get(id = gul_id)
    contexts = {
        'gullar': gullar,
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
            gullar = Gul.objects.create(**gul.cleaned_data)
            return redirect('home', gullar)

    gullar = GulForm
    contexts = {
        'gullar' : gullar,
    }
    return render(request, 'add_gul.html', context = contexts)

def update_gul(request:WSGIRequest, gul_id):
    gul = get_object_or_404(Gul, pk = gul_id)

    if request.method == 'POST':
        form = GulForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            gul.nomi = form.cleaned_data.get('nomi')
            gul.malumot = form.cleaned_data.get('malumot')
            gul.rasm = form.cleaned_data.get('rasm') if form.cleaned_data.get('rasm') else gul.rasm
            gul.created = form.cleaned_data.get('created')
            gul.turi = form.cleaned_data.get('turi')
            gul.save()


    form = GulForm(initial={
        'nomi': gul.nomi,
        'rasm': gul.rasm,
        'malumot':gul.malumot,
        'created': gul.created,
        'turi': gul.turi
    })

    contexts = {
        'form' : form,
        'photo':gul.rasm
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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password_repeat == password:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, 'Akount yaratildi 😍🥰')
                return redirect('login_user')
    context = {
            'form': RegisterForm()
    }
    return render(request, 'auth/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            messages.success(request, 'Xush kelibsiz😍☺️')
            login(request, user)
            return redirect('home')
    context = {
        'form':LoginForm(),
    }
    return render(request, 'auth/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login_user')