from django.shortcuts import render
from .models import Producto 
from django.contrib.auth.decorators import login_required


@login_required(login_url="/autenticacion/logear")
def tienda(request):

    productos= Producto.objects.all()
    return render(request, "tienda/tienda.html",{"productos":productos})