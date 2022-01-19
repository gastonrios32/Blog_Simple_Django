from sre_constants import SUCCESS
from django.http.response import HttpResponse
from django.shortcuts import  render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import *
from django.urls import reverse_lazy


def index (request):
    return render(request,'BlogApp/index.html')

def lectores_lista (request):
    
    lectores= Lector.objects.all()
    return render(request,'BlogApp/lectores_list.html', {"lectores":lectores})

#def nuevaPublicacion(request):
 #   return render(request,'BlogApp/nuevaPublicacion.html')

def publicacion_lista(request):
    lista = Publicacion.objects.all()
    return render(request,'BlogApp/publicacion_list.html', {"lista": lista})

def buscar(request):
    return render(request,'BlogApp/buscar.html')

def buscarPublicacion(request):
    
    busqueda = request.GET.get("busqueda")
    publicacion = Publicacion.objects.all()
    
    if busqueda:
        publicacion = Publicacion.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(fechaCreacion__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    
    return render(request,'BlogApp/buscar.html', {"publicacion": publicacion})


def login (request):
    return render(request,'BlogApp/index.html')

def categorias_lista (request):
    categoria = Categorias.objects.all()
    return render(request,'BlogApp/categoria_list.html', {"categoria":categoria})


class PublicacionList(ListView):
    model = Publicacion
    template_name = "BlogApp/publicacion_list.html"


class PublicacionDetalle(DetailView):
    model = Publicacion
    template_name = "BlogApp/detallePublicacion.html"


class PublicacionCreacion(CreateView):
    model = Publicacion
    success_url = "publicaciones/"
    fields=['nombre','fechaCreacion', 'descripcion']


class PublicacionUpdate(UpdateView):
    model = Publicacion
    success_url = "../../"
    fields=['nombre','fechaCreacion', 'descripcion']

class PublicacionDelete(DeleteView):
    model = Publicacion
    success_url = "../../"
    template_name = 'BlogApp/publicacion_confirm_delete.html'

class CategoriaList(ListView):
    model = Categorias
    template_name = "BlogApp/categoria_list.html"


class CategoriaDetalle(DetailView):
    model = Categorias
    template_name = "BlogApp/detalleCategoria.html"


class CategoriaCreacion(CreateView):
    model = Categorias
    success_url = "publicaciones/"
    fields=['nombreCategoria', 'tipoCategoria']


class CategoriaUpdate(UpdateView):
    model = Categorias
    success_url = "../../"
    fields=['nombreCategoria', 'tipoCategoria']

class CategoriaDelete(DeleteView):
    model = Categorias
    success_url = "../../"
    template_name = 'BlogApp/categoria_confirm_delete.html'

class LectorList(ListView):
    model = Lector
    template_name = "BlogApp/lectores_list.html"


class LectorDetalle(DetailView):
    model = Lector
    template_name = "BlogApp/detalleLector.html"


class LectorCreacion(CreateView):
    model = Lector
    success_url = "publicaciones/"
    fields=['nombre','email', 'fechaIngreso']


class LectorUpdate(UpdateView):
    model = Lector
    success_url = "../../"
    fields=['nombre','email', 'fechaIngreso']

class LectorDelete(DeleteView):
    model = Lector
    success_url = "../../"
    template_name = 'BlogApp/lectores_confirm_delete.html'