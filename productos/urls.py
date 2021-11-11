from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

urlpatterns = [
    path('productos/', views.producto_list, name='productoList'),
    path('producto/<id>', views.single_producto, name='singleProducto'),
    path('productocreate/', csrf_exempt(views.producto_create), name='productoCreate'),
]
