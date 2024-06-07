from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from pedidos.models import LineasPedido, Pedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):

    pedido = Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineasPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    LineasPedido.objects.bulk_create(lineas_pedido)
    enviar_mail(pedido=pedido,
                lineas_pedido=lineas_pedido,
                nombreusuario=request.user.username,
                emailusuario=request.user.email)
    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../")

def enviar_mail(**kawargs):

    asunto="Gracias por el pedido"
    mensaje=render_to_string("email/pedido.html",{"pedido":kawargs.get("pedido"),
                                                  "lineas_pedido": kawargs.get("lineas_pedido"),
                                                  "nombreusuario":kawargs.get("nombreusuario")})
    
    mensaje_texto=strip_tags(mensaje)
    from_email="gonzalo.digangi@gmail.com"
    #to= kawargs.get("emailusuario")
    to= "anothershreklover@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)