from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Configuración del modelo Producto en el panel de administración."""
    list_display = ("nombre", "categoria", "precio", "stock", "reviews")
    list_filter = ("categoria",)
    search_fields = ("nombre",)
