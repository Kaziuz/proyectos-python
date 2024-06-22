from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView  # esto es una plantilla de lista de cosas
from django.views.generic.detail import DetailView # esto es una plantilla para detalle de las cosas
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView # posibilita crear nuevos elementos en las vistas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy # es un redirect

from .models import Tarea

# Create your views here.

# Vista para loguiarse
class Logueo(LoginView):
  template_name = 'base/login.html'
  field = '__all__' # incorpora todos los campos que trae django para el form de login
  redirect_authenticated_user = True
  
  def get_success_url(self):
    # Si se loguea redirecciona al usuario a la lista de tareas
    return reverse_lazy('tareas')
    # return super().get_success_url()

# vista para registrarse
class PaginaRegistro(FormView):
  template_name = 'base/registro.html'
  form_class = UserCreationForm
  redirect_authenticated_user = True
  success_url = reverse_lazy('tareas') # redirecciona a la lista de tareas
  
  def form_valid(self, form):
    usuario = form.save()
    if usuario is not None:
      # establecemos el registro del usuario
      login(self.request, usuario)
    return super(PaginaRegistro, self).form_valid(form)
  
  def get(self, *args, **kwargs):
    # si el usuario esta autenticado, no puede visitar la pagina de registro
    if self.request.user.is_authenticated:
      return redirect('tareas')
    return super(PaginaRegistro, self).get(*args, **kwargs)

# Vista de lista de tareas
# el LoginRequiredMixin hace que no sea posible ver esa vista si no se esta loguiado
class ListaPendientes(LoginRequiredMixin, ListView):
  model = Tarea
  context_object_name = 'tareas' # este tareas es lo que usamos en la template {}
  
  def get_context_data(self, **kwargs):
    # Esta función nos sirve para mostrar solo los datos del usuario loguiado
    context = super().get_context_data(**kwargs)
    # solo muestra las tareas del usuario loguiado
    context['tareas'] = context['tareas'].filter(usuario=self.request.user)
    # Tomamos el campo completo y filtramos las tareas por las que no
    # esten completas
    context['count'] = context['tareas'].filter(completo=False).count()
    
    # Devolvemos solo las tareas que el usuario escribio en el input buscar
    # en la pagina tarea_list
    valor_buscado = self.request.GET.get('area-buscar') or ''
    if valor_buscado:
      context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
      # mantenemos la palabra escrita en el input
      context['valor_buscado'] = valor_buscado
    return context

# vista de detalle de las tareas
class DetalleTarea(LoginRequiredMixin, DetailView):
  model = Tarea
  context_object_name = 'tarea' # este tarea es lo que usamos en la template como variable {}
  template_name = 'base/tarea.html' # esto es para que el framework busque el nombre de esta plantilla

# vista crear tarea  
class CrearTarea(LoginRequiredMixin, CreateView):
  # crea un nuevo pedido y lo incorpora en la lista
  model = Tarea
  # fields = '__all__' # Incorpora todos los campos del modelo tarea
  fields = ['titulo', 'descripcion', 'completo']
  success_url = reverse_lazy('tareas') # cuando haya habido un éxito al llenar el formulario, redirecciona a tareas
  
  def form_valid(self, form):
    # Esto lo que hace es que cada vez que se cree una tarea, la asigna al usuario loguiado
    form.instance.usuario = self.request.user
    return super(CrearTarea, self).form_valid(form)
  
# Editar tarea
class EditarTarea(LoginRequiredMixin, UpdateView):
  model = Tarea
  # fields = '__all__' # Incorpora todos los campos del modelo tarea
  fields = ['titulo', 'descripcion', 'completo']
  success_url = reverse_lazy('tareas') # cuando haya habido un éxito al llenar el formulario, redirecciona a tareas

# eliminar tarea
class EliminarTarea(LoginRequiredMixin, DeleteView):
  model = Tarea
  context_object_name = 'tarea'
  success_url = reverse_lazy('tareas')