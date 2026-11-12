from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


# ---- Vista Basada en Función (FBV): bienvenida ----
def home(request):
    """Página de bienvenida. Usa render() con contexto.

    QuerySet #1 (filtrado): solo productos CON stock disponible.
    Es 'lazy': la consulta a la BD no se ejecuta aquí, sino cuando la
    plantilla lo recorre o se llama a .count().
    """
    disponibles = Producto.objects.filter(stock__gt=0)  # QuerySet lazy
    contexto = {
        "titulo": "Amazon Electronic Store",
        "total": Producto.objects.count(),
        "en_stock": disponibles.count(),  # aquí recién se evalúa
    }
    return render(request, "catalogo/home.html", contexto)


# ---- Vista Basada en Clase (CBV): listar catálogo ----
class ProductoListView(ListView):
    """Lista los productos con stock, ordenados por precio (ListView)."""

    model = Producto
    template_name = "catalogo/catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        """QuerySet #2 (filtrado + ordenado): con stock, por precio ascendente.

        También es 'lazy': Django no consulta la BD hasta que la plantilla
        itera el resultado en el {% for %}.
        """
        return Producto.objects.filter(stock__gt=0).order_by("precio")

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["titulo"] = "Store Catalog"
        return contexto
