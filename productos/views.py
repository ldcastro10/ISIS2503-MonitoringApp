from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import ProductoForm
from .logic.producto_logic import get_productos, get_producto, create_producto
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

@login_required
def producto_list(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        productos = get_productos()
        context = {
            'producto_list': productos
        }
        return render(request, 'Producto/productos.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def single_producto(request, id=0):
    producto = get_producto(id)
    context = {
        'producto': producto
    }
    return render(request, 'Producto/producto.html', context)

@login_required
def producto_create(request):
    role = getRole(request)
    if role == "Gerencia Campus":
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
    else:
        return HttpResponse("Unauthorized User")
