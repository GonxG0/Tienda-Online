from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ProyectoWebApp.urls")),
    path('servicios/', include("servicios.urls")),
    path('blog/', include("blog.urls")),
    path('contacto/', include("contacto.urls")),
    path('tienda/', include("tienda.urls")),
    path('carro/', include("carro.urls")),
    path('autenticacion/', include("autenticacion.urls")),
    path('pedidos/', include("pedidos.urls")),
]
