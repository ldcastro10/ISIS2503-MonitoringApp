from django.shortcuts import render
from .forms import PedidoForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_pedido import create_pedido, get_pedidos
from django.contrib.auth.decorators import login_required

@login_required
def pedido_list(request):
    pedidos = get_pedidos()
    context = {
        'pedido_list': pedidos
    }
    return render(request, 'Pedido/pedidos.html', context)

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            create_pedido(form)
            messages.add_message(request, messages.SUCCESS, 'Pedido create successful')
            return HttpResponseRedirect(reverse('pedidoCreate'))
        else:
            print(form.errors)
    else:
        form = PedidoForm()

    context = {
        'form': form,
    }

    return render(request, 'Pedido/pedidoCreate.html', context)