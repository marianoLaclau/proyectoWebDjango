from django.db import models

# Create your models here.

class CategProductos(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    
    class Meta :
        verbose_name = "CategoriaProd"
        verbose_name_plural = "categoriasProd"
        
        
    def __str__(self) :
        return self.nombre    
        
        

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    categoria = models.ForeignKey(CategProductos,on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to="tienda")
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)
    
    class Meta():
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
    def __str__(self) :
        return self.nombre         