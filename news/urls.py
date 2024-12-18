from django.urls import path

from news.views import asosiy, gul_tur, gul

urlpatterns = [
    path('', asosiy, name="home"),
        path('turlar/<int:tur_id>/', gul_tur, name='turlar'),
        path('gullar/<int:gul_id>/', gul, name='gullar'),
]