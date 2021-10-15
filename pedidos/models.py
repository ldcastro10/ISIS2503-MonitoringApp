from django.db import models
from productos.models import Producto

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    comercio = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)