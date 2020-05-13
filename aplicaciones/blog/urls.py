from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generales/', views.generales, name='generales'),
    path('tutoriales/', views.tutoriales, name='tutoriales'),
    path('videojuegos/', views.videojuegos, name='videojuegos'),
    path('programacion/', views.programacion, name='programacion'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('<slug:slug>/', views.detalle_publicacion, name='detalle_publicacion')
]
