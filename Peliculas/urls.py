from django.urls import path
from Peliculas.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('about/', about, name='about'),
    path('pelicula/', pelicula, name="pelicula"),
    path('peliculasForm', peliculasForm, name="peliculasForm"),
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(template_name='Peliculas/logout.html'), name='logout'),
    #CBV---------------------------------------------------------------------------
    path('peliculas/', PeliculaLista.as_view(), name='pelicula_lista'),
    path('peliculas/<int:pk>/', PeliculaDetalle.as_view(), name='pelicula_detalle'),
    path('peliculas/crear/', PeliculaCrear.as_view(), name='pelicula_crear'),
    path('peliculas/<int:pk>/actualizar/', PeliculaActualizar.as_view(), name='pelicula_actualizar'),
    path('peliculas/<int:pk>/borrar/', PeliculaBorrar.as_view(), name='pelicula_borrar'),
    path('editarUsuario/', UsuarioEdicionView.as_view(), name='editar_usuario'),
    path('cambiar-password/', CambioPasswordView.as_view(), name='cambio_password'),
    path('perfil/', ver_perfil, name='ver_perfil')
]
