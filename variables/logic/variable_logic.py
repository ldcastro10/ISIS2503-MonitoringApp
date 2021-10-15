from ..models import Variable

def get_variables():
    queryset = Variable.objects.all()
    return (queryset)

def create_variable(form):
    pedido = form.save()
    pedido.save()
    return ()