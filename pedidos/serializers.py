from rest_framework import serializers
from . import models


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'producto', 'value', 'unit', 'comercio', 'time',)
        model = models.Pedido