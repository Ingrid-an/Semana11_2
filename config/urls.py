"""Configuración de URLs del proyecto (config)."""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Incluye las rutas de la app catalogo (desacoplamiento con include)
    path("", include("catalogo.urls")),
]
