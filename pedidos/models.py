from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto



# Create your models here.

User = get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "pedido"
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    def __str__(self):
        return str(self.id)


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    subtotal = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    #Obtenemos el precio a traves del objeto producto con el decorador
    @property
    def precio(self):
        return self.producto.precio
    
    
    def __str__(self):
        return f"Has seleccionado {self.cantidad} , {self.producto.nombre}"

    class Meta:
        db_table = "lineapedido"
        verbose_name = "linea_pedido"
        verbose_name_plural = "linea_pedidos"
