from django.urls import path
from BlogApp import views

urlpatterns = [
    path('',views.index, name="Index"),
    path('lectores/',views.lectores, name="Lectores"),
    path('buscar',views.buscar, name="Buscar"),
    path('buscarPublicacion/',views.buscarPublicacion),    
    path('categorias/',views.categorias, name="Categoria"),            
    path('nuevaPublicacion/',views.nuevaPublicacion, name="NuevaPublicacion"),
    path('login/',views.login, name="Login" ),
]