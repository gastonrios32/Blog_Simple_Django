from django.db import models

class Lector(models.Model):
    nombre=models.CharField( max_length=50)
    email=models.CharField( max_length=50)
    fechaIngreso=models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
            return f'{self.nombre}({self.email})'
    
class Publicacion(models.Model):
    nombre=models.CharField( max_length=50)
    fechaCreacion=models.DateField( auto_now=False, auto_now_add=False)
    descripcion=models.CharField( max_length=500)
    def __str__(self):
        return f'{self.nombre}({self.descripcion})'    
    
class Categorias(models.Model):
    nombreCategoria=models.CharField( max_length=50)
    tipoCategoria=models.CharField( max_length=50)
    def __str__(self):
        return f'{self.nombreCategoria}({self.tipoCategoria})'    