from django.urls import path
from .views import VRegistro , cerrar_sesion , ingresar


urlpatterns = [
    
    path("",VRegistro.as_view(),name="Autenticacion"),
    path("Cerrar_sesion",cerrar_sesion,name="Cerrar_sesion"),
    path("Login",ingresar,name="Login")

]
