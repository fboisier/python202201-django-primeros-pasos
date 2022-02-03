from django.urls import path     
from . import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index),	   
    path('hola', views.hola),	   
    path('saluda', views.saludar),	 
    path('saludar/<str:nombre>', views.saludar_nombre),
    path('pancho/crea/una/funcion/<int:cantidad>/hecha/en/django', views.aumenta),
    path('editar/<int:id>', views.editar),

    path('template/uno', views.template_uno)
]