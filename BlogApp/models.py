from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Lector(models.Model):
    nombre=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    fechaIngreso=models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
            return f'{self.nombre} - {self.email}'
    
class Autores(models.Model):
    nombre= models.CharField( max_length=50)
    fechaNacimiento=models.DateField( auto_now=False, auto_now_add=False)
    email=models.CharField( max_length=50)
    GeneroAutor=models.CharField( max_length=50)
    def __str__(self):
            return f'{self.nombre} - {self.GeneroAutor}' 
    
class Categorias(models.Model):
    nombreCategoria=models.CharField( max_length=50)
    tipoCategoria=models.CharField( max_length=50)
    def __str__(self):
        return f'{self.nombreCategoria} - {self.tipoCategoria} -'  


class Publicacion(models.Model):
    nombre=models.CharField( max_length=250)
    fechaCreacion=models.DateField( auto_now=False, auto_now_add=False)
    descripcion=models.CharField( max_length=500)
    imagenPublicacion = models.ImageField(upload_to='publicaciones/',null=True,blank= True)
    contenido = RichTextField (blank=True)
    nombCategoria = models.ForeignKey(Categorias,null=True,blank=True, on_delete=models.CASCADE)
    nombAutor = models.ForeignKey(Autores,null=True,blank=True, on_delete=models.CASCADE)    
    
    class Meta:
        ordering = ('fechaCreacion',)
    
    def __str__(self):
        return f'{self.nombre}'    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True,blank= True)
    
    def __str__(self):
        return f"Imagen de : {self.user.username}"


    

