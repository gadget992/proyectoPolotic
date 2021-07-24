from django.contrib import admin
from django.db import models
from .models import Categoria, Producto


# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)

