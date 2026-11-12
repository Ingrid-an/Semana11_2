"""seed.py - Puebla el catálogo con productos de ejemplo.
Uso:  python manage.py shell < seed.py
"""
from catalogo.models import Producto

Producto.objects.all().delete()

datos = [
    ("Virtual Reality Headset", 199.00, "wearables", 15, 4.0),
    ("Meta Quest 3", 499.00, "wearables", 8, 4.0),
    ("Canon EOS Rebel T7 DSLR", 579.00, "camaras", 5, 4.0),
    ("JBL Go 4", 49.95, "audio", 30, 4.0),
    ("Lenovo Tab One", 89.90, "computo", 12, 4.0),
    ("Keyboard Mecánico", 203.99, "accesorios", 20, 4.0),
    ("Wireless Mouse", 11.69, "accesorios", 50, 4.0),
    ("Luxury Wristwatch", 299.00, "wearables", 0, 4.0),
    ("Raycon Fitness Bluetooth Earbuds", 101.99, "audio", 25, 4.0),
]
for n, p, c, s, r in datos:
    Producto.objects.create(nombre=n, precio=p, categoria=c, stock=s, reviews=r)

print("Productos creados:", Producto.objects.count())
