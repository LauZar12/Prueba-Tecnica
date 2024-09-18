
from django.db import models
from datetime import date

# Clase base Item.
class Item(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fpublicacion = models.DateField()

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Publicado: {self.fpublicacion}"

# Clase derivada 'Libro'.
class Libro(Item):
    cant_paginas = models.IntegerField()

    def mostrar_info(self):
        return f"Libro - {super().mostrar_info()}, Páginas: {self.cant_paginas}"

# Clase derivada 'Revista'
class Revista(Item):
    numero = models.IntegerField()

    def mostrar_info(self):
        return f"Revista - {super().mostrar_info()}, Número: {self.numero}"

# Prestamos
class Prestamo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(default=date.today)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Préstamo dell libro: {self.item.titulo}"

# Clase para gestionar items
class Biblioteca:
    def __init__(self):
        self.items = Item.objects.all()

    def mostrar_info(self):
        for item in self.items:
            print(item.mostrar_info())
