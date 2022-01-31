from django.contrib import admin
from .models import *

#Registra los modelos para administrar desde el admin 

admin.site.register(Lector)
admin.site.register(Publicacion)
admin.site.register(Categorias)
admin.site.register(Autores)
admin.site.register(Avatar)
