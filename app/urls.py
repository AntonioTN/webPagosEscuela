from django.urls import path, re_path
from app import views


urlpatterns = [
    # The home page
    path('', views.index, name='home'),

    path('servicios/', views.servicios, name="servicios"),
    path('estadisticas/', views.estadisticas, name="estadisticas"),
    path('profile/', views.profile, name="profile"),
   

]
