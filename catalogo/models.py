from django.db import models


class Producto(models.Model):
    """Modelo de un producto tecnológico del catálogo (mapea a SQLite)."""

    CATEGORIAS = [
        ("audio", "Audio"),
        ("computo", "Cómputo"),
        ("camaras", "Cámaras"),
        ("accesorios", "Accesorios"),
        ("wearables", "Wearables"),
    ]

    nombre = models.CharField("Nombre", max_length=120)
    precio = models.DecimalField("Precio", max_digits=8, decimal_places=2)
    categoria = models.CharField("Categoría", max_length=20,
                                 choices=CATEGORIAS, default="accesorios")
    stock = models.PositiveIntegerField("Stock", default=0)
    reviews = models.DecimalField("Calificación", max_digits=2,
                                  decimal_places=1, default=4.0)
    creado_en = models.DateTimeField("Fecha de registro", auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-creado_en"]

    def __str__(self):
        """Representación legible del objeto (admin y shell)."""
        return self.nombre
