from rest_framework import serializers
from . import models


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'variable', 'value', 'unit', 'comercio', 'time',)
        model = models.Pedido