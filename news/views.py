from ctypes import py_object

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


from .forms import TurForm, GulForm, RegisterForm, LoginForm, CommentForm
from .models import Turi,Gul, Comment


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

def batafsil(request, gul_id):
    gul = Gul.objects.filter(id = gul_id)
    contexts = {
        'gul': gul,
        'comment': CommentForm(),
        'com':Comment.objects.filter(gul_id=gul_id),
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

def comment_save(request:WSGIRequest, gul_id):
    if request.user.authenticated:
        if request.method == "POST":
            coment = CommentForm(data=request.POST)
            if coment.is_valid():
                gul = get_object_or_404(Gul, pk = gul_id)
                com = Comment.objects.create(
                    text = gul.cleaned_data.get('text'),
                    author = request.user,
                    gul = gul
                )
                messages.success(request, "Comment qo'shildi.")

        return redirect("batafsil", gul_id = gul_id)
    messages.error(request, "Avval ro'yhatdan o'ting")
    return redirect('login_user')

def comment_delete(request, comment_id):
    if request.user.is_aauthenticated:
        comment = get_object_or_404(Comment, pk = comment_id)
        if request.user == comment.author or request.user.is_superuser:
            gul_id = comment.gul.pk
            comment.delete()
            messages.success(request, "Comment o'chirildi")
            return redirect('batafsil', gul_id = gul_id)

    messages.error(request, "Avval ro'yhatdan o'ting")
    return redirect('login_user')

def update_comment(request:WSGIRequest, comment_id):
    comment = get_object_or_404(Comment, pk = comment_id)

    if request.method == 'POST':
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            comment.author = form.cleaned_data.get('author')
            comment.text = form.cleaned_data.get('text')
            comment.created = form.cleaned_data.get('created')
            comment.gul = form.cleaned_data.get('gul')
            comment.save()


    form = CommentForm(initial={
        'author': comment.author,
        'text':comment.text,
        'created': comment.created,
        'gul': comment.gul,
    })

    contexts = {
        'form' : form,
    }
    return render(request, 'add_gul.html', context = contexts)

