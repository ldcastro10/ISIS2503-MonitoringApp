from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'variable',
            'value',
            'unit',
            'comercio',
            #'dateTime',
        ]

        labels = {
            'variable' : 'Variable',
            'value' : 'Value',
            'unit' : 'Unit',
            'comercio' : 'Comercio',
            #'dateTime' : 'Date Time',
        }
