from django import forms


class LectorFormulario(forms.Form):

    nombre=forms.CharField( max_length=50)
    email=forms.CharField( max_length=50)
    fechaIngreso=forms.DateField( auto_now=False, auto_now_add=False)

class PublicacionesFormulario(forms.Form):
    
    nombre=forms.CharField( max_length=50)
    fechaCreacion=forms.DateField( auto_now=False, auto_now_add=False)
    descripcion=forms.CharField( max_length=500)

class CategoriasFormulario(forms.Form):
    
    nombreCategoria=forms.CharField( max_length=50)
    tipoCategoria=forms.CharField( max_length=50)

class LectorFormulario(forms.Form):
    
    nombre=forms.CharField( max_length=50)
    fechaNacimiento=forms.DateField( auto_now=False, auto_now_add=False)
    email=forms.CharField( max_length=50)
    GeneroAutor=forms.CharField( max_length=50)
