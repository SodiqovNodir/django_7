from django.db import models

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