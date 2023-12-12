from django.http import HttpResponse
from django.shortcuts import redirect, render
from .form import PeliculaForm, FormularioEdicion, FormularioCambioPassword
from .models import Pelicula
#importo esto para la vista de registro
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#login
from django.contrib.auth import login, authenticate

from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

#clases basadas en vistas
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

#importo para bloquear vistas
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #bloqueo de clases

from django.contrib.auth.models import User

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.utils.decorators import method_decorator

def inicio(request):
    return render(request, "Peliculas/index.html")

def pelicula(self):
    pelicula = Pelicula(titulo="", director="")
    pelicula.save()
    documentoDeTexto = f"----->Pelicula {Pelicula.titulo} Genero {Pelicula.genero}" 
    return HttpResponse(documentoDeTexto)


def peliculasForm(request):
    if request.method == 'POST':
        miFormulario = PeliculaForm(request.POST) 
        if miFormulario.is_valid():
            
            miFormulario.save()
            return render(request, 'Peliculas/index.html')
    else:
        miFormulario = PeliculaForm()
    return render(request, "Peliculas/peliculasForm.html", {'miFormulario': miFormulario})
#Vista para el registro
def registro(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']
                form.save()
                return render(request,"Peliculas/index.html" ,  {"mensaje":"Usuario Creado :)"})
    else:
            form = UserCreationForm()
            
    return render(request,"Peliculas/registro.html" ,  {"form":form})

#vista para el login
def login_view(request):

    if request.method == "POST": 
        loginForm = AuthenticationForm(request, data = request.POST)
        
        if loginForm.is_valid(): 
            info = loginForm.cleaned_data 
            usuario = info.get("username")
            contraseña = info.get("password")

            user = authenticate(username=usuario, password=contraseña) 

            if user:
                login(request, user)   
                return render(request, "Peliculas/index.html", {"usuario":user})
        
        else:
            return render(request,"Peliculas/index.html", {"mensaje":"DATOS INCORRECTOS"})

    loginForm = AuthenticationForm() 

    return render(request,"Peliculas/login.html", {"form":loginForm} )

#Vista basada en clases  

class PeliculaLista(ListView):
    model = Pelicula
    template_name = 'Peliculas/peliculasLista.html'
    context_object_name = 'peliculas'

class PeliculaDetalle(DetailView):
    model = Pelicula
    template_name = 'Peliculas/peliculasDetalle.html'  
    context_object_name = 'pelicula'

class PeliculaCrear(CreateView):
    model = Pelicula
    template_name = 'Peliculas/peliculasCrear.html'  
    fields = ['titulo', 'director', 'genero']
    success_url = reverse_lazy('pelicula_lista')

class PeliculaActualizar(UpdateView):
    model = Pelicula
    template_name = 'Peliculas/peliculasActualizar.html'  
    fields = ['titulo', 'director', 'genero']
    success_url = reverse_lazy('pelicula_lista')

class PeliculaBorrar(DeleteView):
    model = Pelicula
    template_name = 'Peliculas/peliculasBorrar.html'  
    success_url = reverse_lazy('pelicula_lista')


def about(request):
    return render(request, 'Peliculas/about.html')

@method_decorator(login_required, name='dispatch')

class UsuarioEdicionView(UpdateView):
    model = User
    form_class = FormularioEdicion
    template_name = 'Peliculas/editar_usuario.html'
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        return self.request.user
    
class CambioPasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'Peliculas/passwordCambio.html'  
    success_url = reverse_lazy('password_exitoso')  

    def form_valid(self, form):
        
        return super().form_valid(form)

    def form_invalid(self, form):
        
        return super().form_invalid(form)
    
@login_required
def ver_perfil(request):
    return render(request, 'Peliculas/perfil.html')
