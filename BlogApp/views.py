from ast import Pass
from django.http.response import HttpResponse
from django.shortcuts import  render
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index (request):
    return render(request,'BlogApp/index.html')

@login_required
def lectores_lista (request):
    
    lectores= Lector.objects.all()
    return render(request,'BlogApp/lectores_list.html', {"lectores":lectores})

@login_required
def autores_lista (request):
    
    listaautores= Autores.objects.all()
    return render(request,'BlogApp/Autores_list.html', {"listaautores":listaautores})

@login_required
def publicacion_lista(request):
    lista = Publicacion.objects.all()
    return render(request,'BlogApp/publicacion_list.html', {"lista": lista})

@login_required
def buscadaPublicacion(request):
    return render(request,'BlogApp/busqueda.html')

@login_required
def buscar(request):
    
    if(request.method == 'GET'):
        nombre = request.GET["nombre"]
        publicaciones = Publicacion.objects.filter(nombre=nombre)
        return render(request, 'BlogApp/resultadobusqueda.html', {'publicaciones':publicaciones , 'nombre':nombre} )
    
    else:
        respuesta = "No enviaste datos"
        
        return HttpResponse(respuesta)


@login_required
def categorias_lista (request):
    categoria = Categorias.objects.all()
    return render(request,'BlogApp/categoria_list.html', {"categoria":categoria})


class PublicacionList(LoginRequiredMixin,ListView):
    model = Publicacion
    template_name = "BlogApp/publicacion_list.html"


class PublicacionDetalle(LoginRequiredMixin,DetailView):
    model = Publicacion
    template_name = "BlogApp/detallePublicacion.html"


class PublicacionCreacion(LoginRequiredMixin,CreateView):
    model = Publicacion
    success_url = "publicaciones/"
    fields=['nombre','fechaCreacion', 'descripcion']


class PublicacionUpdate(LoginRequiredMixin,UpdateView):
    model = Publicacion
    success_url = "../../"
    fields=['nombre','fechaCreacion', 'descripcion']

class PublicacionDelete(LoginRequiredMixin,DeleteView):
    model = Publicacion
    success_url = "../../"
    template_name = 'BlogApp/publicacion_confirm_delete.html'

class CategoriaList(LoginRequiredMixin,ListView):
    model = Categorias
    template_name = "BlogApp/categoria_list.html"


class CategoriaDetalle(LoginRequiredMixin,DetailView):
    model = Categorias
    template_name = "BlogApp/detalleCategorias.html"


class CategoriaCreacion(LoginRequiredMixin,CreateView):
    model = Categorias
    success_url = "categorias/"
    fields=['nombreCategoria', 'tipoCategoria']


class CategoriaUpdate(LoginRequiredMixin,UpdateView):
    model = Categorias
    success_url = "../../"
    fields=['nombreCategoria', 'tipoCategoria']

class CategoriaDelete(LoginRequiredMixin,DeleteView):
    model = Categorias
    success_url = "../../"
    template_name = 'BlogApp/categoria_confirm_delete.html'

class LectorList(ListView):
    model = Lector
    template_name = "BlogApp/lectores_list.html"


class LectorDetalle(LoginRequiredMixin,DetailView):
    model = Lector
    template_name = "BlogApp/detalleLector.html"


class LectorCreacion(LoginRequiredMixin,CreateView):
    model = Lector
    success_url = "lectores/"
    fields=['nombre','email', 'fechaIngreso']


class LectorUpdate(LoginRequiredMixin,UpdateView):
    model = Lector
    success_url = "../../"
    fields=['nombre','email', 'fechaIngreso']

class LectorDelete(LoginRequiredMixin,DeleteView):
    model = Lector
    success_url = "../../"
    template_name = 'BlogApp/lectores_confirm_delete.html'

class AutoresList(LoginRequiredMixin,ListView):
    model = Autores
    template_name = "BlogApp/Autores_list.html"


class AutoresDetalle(LoginRequiredMixin,DetailView):
    model = Autores
    template_name = "BlogApp/detalleAutores.html"


class AutoresCreacion(LoginRequiredMixin,CreateView):
    model = Autores
    success_url = "Autores/"
    fields=['nombre','fechaNacimiento', 'email', 'GeneroAutor']


class AutoresUpdate(LoginRequiredMixin,UpdateView):
    model = Autores
    success_url = "../../"
    fields=['nombre','fechaNacimiento', 'email', 'GeneroAutor']

class AutoresDelete(LoginRequiredMixin,DeleteView):
    model = Autores
    success_url = "../../"
    template_name = 'BlogApp/Autores_confirm_delete.html'

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm (request, data = request.POST)
    
        if form.is_valid():
            
            data = form.cleaned_data
        
            user = authenticate(username=data['username'], password=data['password'])
        
            if user is not None :
                login(request, user)
            
                return render(request, "BlogApp/index.html", {"mensaje" : f"Bienvenido {user.get_username()}"} )
            else:
                return render (request, "BlogApp/index.html", {"mensaje" : f"Usuario o Contraseña Incorrecta"} )
        else:
            return render(request, "BlogApp/index.html", {"mensaje" : f"Error, formulario erroneo"} )

    else:
        form = AuthenticationForm()
        return render (request, "BlogApp/login.html", {'form':form})

def register (request):
    if (request.method == 'POST'):
        form = UserCreationForm (request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            form.save()
            return render (request, "BlogApp/index.html", {"mensaje" :"Usuario Creado  "} )
    else:
        form= UserCreationForm()
        return render(request,'BlogApp/register.html',{"form":form})