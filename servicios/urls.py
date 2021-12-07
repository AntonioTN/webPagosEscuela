from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios, name="servicios"),
    path ('constancia/', views.constancia, name="constancia"),
    path('kardex/', views.kardex, name="kardex"),
    path('seguro/', views.seguro, name="seguro"),
]