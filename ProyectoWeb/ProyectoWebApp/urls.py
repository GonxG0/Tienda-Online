from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from ProyectoWebApp import views

urlpatterns = [
    path('', views.home, name="Home"),
]

# Agrega el nombre de la aplicación a la ruta de los archivos multimedia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
