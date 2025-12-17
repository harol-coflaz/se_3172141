from django.urls import path

from se_core.vistas.navegación.principal import index, acerca_de, mision_vision, contáctanos, inicio_sesion, loginn
urlpatterns = [
    path('', index, name='index'),
    path('acerca_de/', acerca_de, name='acerca_de'),
    path('mision_vision/', mision_vision, name='mision_vision'),
    path('contáctanos/', contáctanos, name='contáctanos'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion'),
    path('login/', loginn, name='login'),
]