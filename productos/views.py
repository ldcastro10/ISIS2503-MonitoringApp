from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ProductoForm
from .logic.producto_logic import get_productos, create_producto

def producto_list(request):
    productos = get_productos()
    context = {
        'producto_list': productos
    }
    return render(request, 'Producto/productos.html', context)

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created producto')
            return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }
    return render(request, 'Producto/productoCreate.html', context)