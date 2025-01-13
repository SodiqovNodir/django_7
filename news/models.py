from django.db import models
from django.contrib.auth.models import User

class Turi(models.Model):
    nomi = models.CharField(max_length=50)
    malumot = models.TextField()
    rasm = models.ImageField(upload_to='turlar/photo', blank=True, null=True)

    def __str__(self):
        return self.nomi

class Gul(models.Model):
    nomi = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='gullar/photo', blank=True, null=True)
    malumot = models.TextField()
    created = models.DateTimeField(auto_now=True)
    turi = models.ForeignKey(Turi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomi

class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    gul = models.ForeignKey(Gul, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} | {self.gul.name[:20]} | {self.text[:20]}"