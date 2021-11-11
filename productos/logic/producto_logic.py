from ..models import Producto

def get_productos():
    queryset = Producto.objects.all()
    return (queryset)

def get_producto(id):
    producto = Producto.objects.raw("SELECT * FROM productos_producto WHERE id=%s" % id)[0]
    return (producto)

def create_producto(form):
    pedido = form.save()
    pedido.save()
    return ()
