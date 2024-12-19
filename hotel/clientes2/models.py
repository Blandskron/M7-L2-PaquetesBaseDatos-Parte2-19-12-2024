from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Reserva(models.Model):
    numero_habitacion = models.CharField(max_length=5)
    ingreso = models.DateField()
    salida = models.DateField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Habitacion N° {self.numero_habitacion} - {self.cliente.nombre} - {self.cliente.apellido}"
    