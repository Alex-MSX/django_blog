from django.shortcuts import render
from . import models
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

app_name='blog'
PAGS = 1

def index(request):
    queryset = request.GET.get('buscar')
    publicaciones = models.Publicacion.objects.filter(estado=True)

    if queryset:
        publicaciones = models.Publicacion.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset), estado=True).distinct()

    paginator = Paginator(publicaciones, PAGS)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    context = {'publicaciones':publicaciones}
    return render(request, 'index.html', context)

def generales(request):
    queryset = request.GET.get('buscar')
    publicaciones = models.Publicacion.objects.filter(estado=True, categoria=models.Categoria.objects.get(nombre__iexact='general'))

    if queryset:
        publicaciones = models.Publicacion.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=models.Categoria.objects.get(nombre__iexact='general')
        ).distinct()

    paginator = Paginator(publicaciones, PAGS)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    context = {'publicaciones':publicaciones}
    return render(request, 'generales.html', context)

def programacion(request):
    queryset = request.GET.get('buscar')
    publicaciones = models.Publicacion.objects.filter(estado=True, categoria=models.Categoria.objects.get(nombre__iexact='programacion'))

    if queryset:
        publicaciones = models.Publicacion.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=models.Categoria.objects.get(nombre__iexact='programacion')
        ).distinct()

    paginator = Paginator(publicaciones, PAGS)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    context = {'publicaciones':publicaciones}
    return render(request, 'programacion.html', context)

def tutoriales(request):
    queryset = request.GET.get('buscar')
    publicaciones = models.Publicacion.objects.filter(estado=True, categoria=models.Categoria.objects.get(nombre__iexact='tutoriales'))

    if queryset:
        publicaciones = models.Publicacion.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=models.Categoria.objects.get(nombre__iexact='tutoriales')
        ).distinct()

    paginator = Paginator(publicaciones, PAGS)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    context = {'publicaciones':publicaciones}
    return render(request, 'tutoriales.html', context)

def tecnologia(request):
    queryset = request.GET.get('buscar')
    publicaciones = models.Publicacion.objects.filter(estado=True, categoria=models.Categoria.objects.get(nombre__iexact='tecnologia'))

    if queryset:
        publicaciones = models.Publicacion.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=models.Categoria.objects.get(nombre__iexact='tecnologia')
        ).distinct()

    paginator = Paginator(publicaciones, PAGS)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    context = {'publicaciones':publicaciones}
    return render(request, 'tecnologia.html', context)

def videojuegos(request):
    queryset = request.GET.get('buscar')
    publicaciones = models.Publicacion.objects.filter(estado=True, categoria=models.Categoria.objects.get(nombre__iexact='videojuegos'))

    if queryset:
        publicaciones = models.Publicacion.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado=True,
            categoria=models.Categoria.objects.get(nombre__iexact='videojuegos')
        ).distinct()

    paginator = Paginator(publicaciones, PAGS)
    page = request.GET.get('page')
    publicaciones = paginator.get_page(page)

    context = {'publicaciones':publicaciones}
    return render(request, 'videojuegos.html', context)

def detalle_publicacion(request, slug):
    publicacion = models.Publicacion.objects.get(slug=slug)
    context = {'publicacion':publicacion}
    return render(request, 'post.html', context)
