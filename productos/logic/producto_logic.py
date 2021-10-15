from ..models import Producto

def get_productos():
    queryset = Producto.objects.all()
    return (queryset)

def create_producto(form):
    pedido = form.save()
    pedido.save()
    return ()