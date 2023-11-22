from django.urls import path
from Peliculas.views import *

urlpatterns = [
    path('', inicio, name="home"),
    path('pelicula/', pelicula, name="pelicula"),
    path('peliculaForm', peliculaForm, name="peliculaForm"),
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(template_name='Peliculas/logout.html'), name='logout'),
    #CBV---------------------------------------------------------------------------
    path('lista/', PeliculaLista.as_view(), name = "PeliculaLista"),
    path('nuevo/',PeliculaCrear.as_view(), name = "PeliculaCrearNuevo"),
    path('<pk>/', PeliculaDetalle.as_view(), name = "PeliculaDetalle"),
    path('<pk>/editar/', PeliculaActualizar.as_view(), name = "PeliculaActualizar"),
    path('<pk>/borrar/', PeliculaBorrar.as_view(), name = "PeliculaBorrar"),
]
