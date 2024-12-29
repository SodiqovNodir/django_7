from django.urls import path

from news.views import asosiy, gul_tur, gul, add_tur, add_gul, batafsil, update_gul, update_tur, register, login_user, logout_user

urlpatterns = [
    path('', asosiy, name="home"),
    path('tur/<int:turi_id>/', gul_tur, name='tur'),
    path('gul/<int:gul_id>/', gul, name='gul'),
    path('gul/<int:gul_id>/', batafsil, name='batafsil'),
    path('gul/<int:gul_id>/update', update_gul, name = 'update_gul'),
    path('tur/<int:turi_id>/update', update_tur, name='update_tur'),

    path('auth/register/', register, name = 'register'),
    path('auth/login/', login_user, name = 'login_user'),
    path('auth/logout/', logout_user, name='logout'),

    path('tur/add/', add_tur, name='add_tur'),
    path('gul/add/', add_gul, name='add_gul'),

]