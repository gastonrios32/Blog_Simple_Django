from django.http.response import HttpResponse
from django.shortcuts import  render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm,AvatarFormulario

@login_required
def index (request):
    publicaciones = Publicacion.objects.all()
    ultimaPublicacion =  reversed(publicaciones)
    
    avatar  = Avatar.objects.filter(user=request.user.id)
    
    return render(request,'BlogApp/index.html', {"ultimaPublicacion": ultimaPublicacion, "url": avatar[0].imagen.url })

@login_required
def lectores_lista (request):
    
    lectores= Lector.objects.all()
    return render(request,'BlogApp/lectores_list.html', {"lectores":lectores})

@login_required
def autores_lista (request):
    avatar  = Avatar.objects.filter(user=request.user.id )
    listaautores= Autores.objects.all()
    return render(request,'BlogApp/Autores_list.html', {"listaautores":listaautores, "url": avatar[0].imagen.url})

@login_required
def publicacion_lista(request):
    avatar  = Avatar.objects.filter(user=request.user.id )
    lista = Publicacion.objects.all()
    return render(request,'BlogApp/publicacion_list.html', {"lista": lista,"url": avatar[0].imagen.url})

@login_required
def buscadaPublicacion(request):
    
    avatar  = Avatar.objects.filter(user=request.user.id )
    
    return render(request,'BlogApp/busqueda.html', {"url": avatar[0].imagen.url} )

@login_required
def buscar(request):
    
    avatar  = Avatar.objects.filter(user=request.user.id )
    
    if(request.method == 'GET'):
        nombre = request.GET["nombre"]
        publicaciones = Publicacion.objects.filter(nombre=nombre)
        return render(request, 'BlogApp/resultadobusqueda.html', {'publicaciones':publicaciones , 'nombre':nombre, "url": avatar[0].imagen.url} )
    
    else:
        respuesta = "No enviaste datos"
        
        return HttpResponse(respuesta)


@login_required
def categorias_lista (request):
    avatar  = Avatar.objects.filter(user=request.user.id )    
    categoria = Categorias.objects.all()
    return render(request,'BlogApp/categoria_list.html', {"categoria":categoria, "url": avatar[0].imagen.url})


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
                
                avatar  = Avatar.objects.filter(user=request.user.id)
            
                return render(request, "BlogApp/index.html", {"mensaje" : f"Bienvenido {user.get_username()}","url": avatar[0].imagen.url } )
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


def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        miform= UserEditForm(request.POST)
        if miform.is_valid():
            
            informacion = miform.cleaned_data
            
            usuario.email= informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion ['first_name']
            usuario.save()
            
            return render (request, "BlogApp/index.html", {"mensaje" :"Usuario Modificado  "})
    else:
        miform = UserEditForm(initial={'email':usuario.email,'first_name':usuario.first_name, 'last_name': usuario.last_name })
        
    return render (request, "BlogApp/editarPerfil.html", {"miform":miform,"usuario":usuario})
            
            
# @login_required
# def agregarAvatar(request):
    
#     avatar = request.user
    
#     if request.POST == 'POST':
#         miformulario = AvatarFormulario ( request.POST, request.FILES )
        
#         if miformulario.isvalid():
#             informacion = miformulario.cleaned_data
            
#             avatar.imagen= informacion['imagen']
#             # avatar.password1 = informacion['password1']
#             # avatar.password2 = informacion['password2']
            
#             avatar.save()
#             return render (request, "BlogApp/index.html", {"mensaje" :" Avatar Asignado "})
#     else:
#         miformulario = AvatarFormulario()
    
#     return render (request, "BlogApp/agregarAvatar.html", {"miformulario":miformulario})


# @login_required
# def agregarAvatar(request):
#     if request.POST == 'POST':
#         miformulario = AvatarFormulario ( request.POST, request.FILES )
        
#         if miformulario.isvalid():
            
#             informacion = miformulario.cleaned_data
            
#             avatar = Avatar (user = informacion['user'],imagen = informacion['imagen'])
#             # Avatar.user = User.objects.get(username = request.user)
#             # Avatar.imagen= miformulario.cleaned_data['imagen']
#             avatar.save()
#             return render (request, "BlogApp/index.html", {"mensaje" :" Avatar Asignado "})
#     else:
#         miformulario = AvatarFormulario()
    
#     return render (request, "BlogApp/agregarAvatar.html", {"miformulario":miformulario})

def agregarAvatar(request):
    if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django
                
                avatar = Avatar (user = request.user, imagen=miFormulario.cleaned_data['imagen']) 
      
                avatar.save()

                return render (request, "BlogApp/index.html", {"mensaje" :" Avatar Asignado "})

    else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

    return render (request, "BlogApp/agregarAvatar.html", {"miFormulario":miFormulario})


