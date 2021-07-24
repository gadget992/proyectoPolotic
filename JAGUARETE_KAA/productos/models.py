from django.db import models

# Create your models here.
class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)


    #con esto especificamos con el nombre que queremos que aparezca en la BBDD
    class Meta():
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
    
    def __str__(self):
        return self.descripcion

        
class Producto(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to = 'producto')
    categoria = models.ManyToManyField(Categoria)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"
    
    def __str__(self):
        return self.titulo
