from django.http.response import HttpResponse
from django.shortcuts import  render
from django.http import HttpResponse

from .models import Publicacion


def index (request):
    return render(request,'BlogApp/index.html')

def lectores (request):
    return render(request,'BlogApp/lectores.html')

def nuevaPublicacion(request):
    return render(request,'BlogApp/nuevaPublicacion.html')

def buscar(request):
    return render(request,'BlogApp/buscar.html')

def buscarPublicacion(request):
    #respuesta = f"Buscando la Publicacion: {request.GET['nombre'] }"
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        descripcion = Publicacion.objets.filter(nombre__icontains=nombre)
        return render(request,'BlogApp/buscar.html',{"nombre":nombre, "descripcion": descripcion})
    else:
        respuesta = "No se encuentra la publicacion "
    
    return HttpResponse(respuesta)

def login (request):
    return render(request,'BlogApp/index.html')

def categorias (request):
    return render(request,'BlogApp/categorias.html')