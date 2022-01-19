from django.urls import path
from BlogApp import views

urlpatterns = [
    path('',views.index, name="Index"),
    path('lectores/',views.lectores_lista, name="Lectores"),
    path('busquedaPublicacion/',views.buscadaPublicacion, name="busquedaPublicacion"),    
    path('buscar/',views.buscar, name="Buscar"),  
    path('categorias/',views.categorias_lista, name="Categoria"),
    path('publicaciones/',views.publicacion_lista, name="Publicaciones"),      
    path('login/',views.login, name="Login" ),
    
    path('listaPublicaciones',views.PublicacionList.as_view(), name="lista" ), 
    path('detallePublicacion/<pk>/',views.PublicacionDetalle.as_view(), name="detail" ), 
    path('NuevaPublicacion',views.PublicacionCreacion.as_view(), name="new" ), 
    path('actualizaPublicaciones/<pk>/',views.PublicacionUpdate.as_view(), name="edit" ), 
    path('eliminaPublicaciones/<pk>/',views.PublicacionDelete.as_view(), name="delete" ),

    path('listaCategoria',views.CategoriaList.as_view(), name="listaCategoria" ), 
    path('detalleCategoria/<pk>/',views.CategoriaDetalle.as_view(), name="detailCategoria" ), 
    path('NuevaCategoria',views.CategoriaCreacion.as_view(), name="newCategoria" ), 
    path('actualizaCategoria/<pk>/',views.CategoriaUpdate.as_view(), name="editCategoria" ), 
    path('eliminaCategoria/<pk>/',views.CategoriaDelete.as_view(), name="deleteCategoria" ), 

    path('listaLector',views.LectorList.as_view(), name="listaLector" ), 
    path('detalleLector/<pk>/',views.LectorDetalle.as_view(), name="detailLector" ), 
    path('NuevoLector',views.LectorCreacion.as_view(), name="newLector" ), 
    path('actualizaLector/<pk>/',views.LectorUpdate.as_view(), name="editLector" ), 
    path('eliminaLector/<pk>/',views.LectorDelete.as_view(), name="deleteLector" ),                   
]