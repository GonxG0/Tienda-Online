from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]