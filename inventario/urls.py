from django.urls import path
from . import views

urlpatterns = [
    path('estructura/', views.estructura_list, name='estructura_list')
]
