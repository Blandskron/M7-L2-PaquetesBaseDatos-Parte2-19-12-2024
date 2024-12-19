from django.shortcuts import render
from .models import Clientes, Reserva

# Create your views here.
def lista_clientes2(request):
    clientes = Clientes.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def lista_reservas2(request):
    reservas = Reserva.objects.all()
    return render(request, 'lista_reservas.html', {'reservas': reservas})
