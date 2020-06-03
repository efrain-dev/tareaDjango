from django.contrib import admin
from gestionForm.models import Cliente, Producto, Project, Trabajador, Marca


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", 'telefono')
    search_fields = ("nombre", "telefono")


class ProductoAdmin(admin.ModelAdmin):
    list_filter = ("nombre", "marca")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Trabajador)
admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Project)
