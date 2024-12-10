from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('trajes/', views.trajes, name='trajes'), 
    path('tenis/', views.tenis, name='tenis'),
    path('playeras/', views.playeras, name='playeras'),
    path('pantalones/', views.pantalones, name='pantalones'),
    path('lentes', views.lentes, name='lentes'),
    path('chumpas', views.chumpas, name='chumpas'),
    path('descuentos', views.descuentos, name='descuentos'),
    path('accesorios', views.accesorios, name='accesorios'),
    path('carrito', views.carrito, name='carrito'),
    path('registro', views.registro, name='registro'),

]
