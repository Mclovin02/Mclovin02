from django.db import models
from django.utils import timezone

# Create your models here.


class Usuarios(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    email_usuario = models.EmailField()


    def __str__(self):
        return f"nombre de usuario: {self.nombre_usuario} ,email usuario: {self.email_usuario}"

class Productos(models.Model):
    nombre_producto = models.CharField(max_length=30)

    def __str__(self):
        return f'Nombre producto: {self.nombre_producto}'

class Ventas_Detalles(models.Model):
    monto = models.FloatField()
    fecha_venta = models.DateField()
    forma_de_pago = models.CharField(max_length=25)
    Producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)

    def __str__(self):
        return f'Monto:{self.monto},fecha venta: {self.fecha_venta}, Forma de pago: {self.forma_de_pago}, producto:{self.Producto},usuario :{self.usuario}'
    


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f'Mensaje de {self.nombre} - {self.email}'
    



    