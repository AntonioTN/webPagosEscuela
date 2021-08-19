from django.urls import path
from . import views

urlpatterns = [
    path('', views.alumnos, name="alumnos"),
    path ('agregar/', views.agregar, name="agregar"),
    path ('eliminar/<int:alumno_id>/', views.eliminar, name="eliminar"),
    path ('editar/<int:alumno_id>/', views.editar, name="editar"),
]