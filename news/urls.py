from django.urls import path

from news.views import asosiy, gul_tur, gul, add_tur, add_gul

urlpatterns = [
    path('', asosiy, name="home"),
    path('tur/<int:turi_id>/', gul_tur, name='tur'),
    path('gul/<int:gul_id>/', gul, name='gul'),
    path('tur/add/', add_tur, name='add_tur'),
    path('gul/add/', add_gul, name='add_gul'),
]