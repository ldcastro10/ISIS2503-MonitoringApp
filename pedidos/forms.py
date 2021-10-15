from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'producto',
            'value',
            'unit',
            'comercio',
            #'dateTime',
        ]

        labels = {
            'producto' : 'Producto',
            'value' : 'Value',
            'unit' : 'Unit',
            'comercio' : 'Comercio',
            #'dateTime' : 'Date Time',
        }
