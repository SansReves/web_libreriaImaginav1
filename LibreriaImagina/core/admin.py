from django.contrib import admin
from .models import CatgLibro,Cliente,Despacho,Empleado,Estado,Libro,OrdenCompra,OrdenDespacho,OrdenLibro,OrdenServicio,Servicio,TipoCliente,TipoEmpleado,TipoPago
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    list_display = ["nombre_libro","autor_libro","sinopsis_libro","imagen_libro","precio_libro","stock_libro","id_catg"]
    list_editable = ["nombre_libro","autor_libro","sinopsis_libro","precio_libro"]
    search_fields = ["nombre_libro","autor_libro","id_catg"]
    list_filter = ["autor_libro","id_catg"]
    list_per_page = 1




admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(CatgLibro)
admin.site.register(Despacho)
admin.site.register(Empleado)
admin.site.register(Estado)
admin.site.register(OrdenCompra)
admin.site.register(OrdenDespacho)
admin.site.register(OrdenLibro)
admin.site.register(OrdenServicio)
admin.site.register(Servicio)
admin.site.register(TipoCliente)
admin.site.register(TipoEmpleado)
admin.site.register(TipoPago)
