from django.urls import path
from BlogApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.index, name="Index"),
    path('about/',views.acercaDeMi, name="about"),
    path('lectores/',views.lectores_lista, name="Lectores"),
    path('Autores/',views.autores_lista, name="Autores"),    
    path('busquedaPublicacion/',views.buscadaPublicacion, name="busquedaPublicacion"),    
    path('buscar/',views.buscar, name="Buscar"),  
    path('categorias/',views.categorias_lista, name="Categoria"),   
    path('login',views.login_request, name="Login" ),
    path('register/',views.register, name="register" ),    
    path('logout',LogoutView.as_view(template_name = 'BlogApp/logout.html'), name="Logout" ),
    path('editarPerfil/',views.editarPerfil, name="EditarPerfil" ),
    path('agregarAvatar/',views.agregarAvatar, name="agregarAvatar" ),                 
    path('contacto/',views.Contactame, name="contacto" ),       
    
    path('publicaciones/',views.PublicacionList.as_view(), name="Publicaciones" ), 
    path('detallePublicacion/<pk>/',views.PublicacionDetalle.as_view(), name="detail" ), 
    path('NuevaPublicacion/',views.PublicacionCreacion.as_view(), name="new" ), 
    path('actualizaPublicaciones/<pk>/',views.PublicacionUpdate.as_view(), name="edit" ), 
    path('eliminaPublicaciones/<pk>/',views.PublicacionDelete.as_view(), name="delete" ),

    path('listaCategoria',views.CategoriaList.as_view(), name="listaCategoria" ), 
    path('detalleCategorias/<pk>/',views.CategoriaDetalle.as_view(), name="detailCategoria" ), 
    path('NuevaCategoria',views.CategoriaCreacion.as_view(), name="newCategoria" ), 
    path('actualizaCategoria/<pk>/',views.CategoriaUpdate.as_view(), name="editCategoria" ), 
    path('eliminaCategoria/<pk>/',views.CategoriaDelete.as_view(), name="deleteCategoria" ), 

    path('listaLector',views.LectorList.as_view(), name="listaLector" ), 
    path('detalleLector/<pk>/',views.LectorDetalle.as_view(), name="detailLector" ), 
    path('NuevoLector',views.LectorCreacion.as_view(), name="newLector" ), 
    path('actualizaLector/<pk>/',views.LectorUpdate.as_view(), name="editLector" ), 
    path('eliminaLector/<pk>/',views.LectorDelete.as_view(), name="deleteLector" ),  
    
    path('listaAutores',views.AutoresList.as_view(), name="listaAutores" ), 
    path('detalleAutores/<pk>/',views.AutoresDetalle.as_view(), name="detailAutor" ), 
    path('NuevoAutor',views.AutoresCreacion.as_view(), name="newAutor" ), 
    path('actualizaAutores/<pk>/',views.AutoresUpdate.as_view(), name="editAutor" ), 
    path('eliminaAutores/<pk>/',views.AutoresDelete.as_view(), name="deleteAutor" ),                        
]