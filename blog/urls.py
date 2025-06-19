from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_public, name=' lista_public'),
    path('evaluacion2/', views.equipos_lista, name=' equipos_lista'),
]
