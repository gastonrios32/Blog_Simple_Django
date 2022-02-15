from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor import *

from .models import *


class LectorFormulario(forms.Form):

    nombre=forms.CharField( max_length=50)
    email=forms.CharField( max_length=50)
    fechaIngreso=forms.DateField()

class PublicacionesFormulario(forms.Form):
    
    nombre=forms.CharField( max_length=250)
    fechaCreacion=forms.DateField()
    descripcion=forms.CharField( max_length=500)
    imagenPublicacion = forms.ImageField(required=False)  
    contenido = RichTextField()
    nombCategoria = forms.CharField(max_length="150")
    nombAutor =  forms.CharField(max_length="150")
    
    class Meta:
            model = Publicacion
            fields = ['nombre','fechaCreacion', 'descripcion' ,'imagenPublicacion','contenido','nombCategoria','nombAutor']
            help_texts = {k:"" for k in fields}
    

class CategoriasFormulario(forms.Form):
    
    nombreCategoria=forms.CharField( max_length=50)
    tipoCategoria=forms.CharField( max_length=50)

class LectorFormulario(forms.Form):
    
    nombre=forms.CharField( max_length=50)
    fechaNacimiento=forms.DateField( )
    email=forms.CharField( max_length=50)
    GeneroAutor=forms.CharField( max_length=50)

class UserEditForm(UserCreationForm):
    email= forms.EmailField(label= "Modificar Email")
    password1 = forms.CharField(label= "Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la contraseña",widget=forms.PasswordInput)
    last_name = forms.CharField(label= "Ingrese su Apellido")
    first_name = forms.CharField(label= "Ingrese su Nombre")
    
    class Meta:
        model = User
        fields = ['email','password1','password2','last_name','first_name']
        help_texts = {k:"" for k in fields}
        
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

    class Meta:
        model = Avatar
        fields = ['imagen']
        help_texts = {k:"" for k in fields}