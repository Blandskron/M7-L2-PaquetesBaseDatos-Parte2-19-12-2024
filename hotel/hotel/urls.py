"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clientes.views import lista_clientes, lista_reservas
from clientes2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', lista_clientes, name='clientes'),
    path('reservas/', lista_reservas, name='reservas'),
    path('clientes2/', views.lista_clientes2, name='clientes2'),
    path('reservas2/', views.lista_reservas2, name='reservas2'),
]
