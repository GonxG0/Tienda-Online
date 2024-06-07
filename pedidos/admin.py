from django.contrib import admin

from .models import Pedido, LineasPedido

admin.site.register([Pedido,LineasPedido])
