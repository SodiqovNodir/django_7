from idlelib.autocomplete import FILES

from django import forms

from news.models import Turi


class TurForm(forms.Form):
    nomi = forms.CharField(max_length=50, widget=forms.TextInput())
    malumot = forms.CharField(widget=forms.Textarea())
    rasm = forms.ImageField(widget=forms.FileInput())

class GulForm(forms.Form):
    nomi = forms.CharField(widget=forms.TextInput())
    rasm = forms.ImageField(widget=forms.FileInput())
    malumot = forms.CharField(widget=forms.Textarea())
    created = forms.DateTimeField(widget=forms.DateTimeInput())
    turi = forms.ModelChoiceField(queryset=Turi.objects.all(), widget=forms.Select())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
    password_repeat = forms.CharField(min_length=8, widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput())
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())

