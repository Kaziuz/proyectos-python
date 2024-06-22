from django.db import models
from django.contrib.auth.models import User # tabla de usuarios creada por django

# Create your models / tables here.
# Se debe de crear una clase que represente la tabla

class Tarea(models.Model):
  usuario = models.ForeignKey(User,
                              on_delete=models.CASCADE, # si se elimina este usuario, todos lo relacionado a el tmb se elimina
                              null=True, # El valor de usuario puede estar vacio
                              blank=True # Si hacemos un formulario que pide un registro, este campo puede estar vacio 
                            )
  titulo = models.CharField(max_length=200)
  descripcion = models.TextField(null=True, blank=True)
  completo = models.BooleanField(default=False)
  creado = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    # Si pedimos una tarea, se imprime el titulo de la tarea
    return self.titulo

  # Definimos una clase Meta dentro de nuestra clase tarea para definir las opciones de la tabla
  class Meta:
    # como se van a ordenar las tareas dentro de nuestra tabla, por el campo completo
    ordering = ['completo']
  
