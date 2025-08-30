from django.urls import path
from . import views

# ACA 
# PRIMER ARGUMENTO = ARMO EL CAMINO QUE LE QUIERO DAR A LA URL
# SEGUNDO ARGUMENTO = VA EL NOMBRE DE LA FUNCION QUE VA A SER LLAMADA  - ESA FUNCION LA DEFINO O CREO EN VIEWS.PY DE LA APLICACION
# TERCER ARGUMENTO = ES EL NOMBRE CON EL QUE VA A SER LLAMADA LA FUNCION

urlpatterns = [
    path('', views.index, name='index'),
    path('estructura/', views.estructura_list, name='estructura_list'), 
    path('estructura/nuevo', views.estructura_create, name='estructura_create')
]
