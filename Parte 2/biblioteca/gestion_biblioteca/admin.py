from django.contrib import admin
from .models import Libro, Revista, Prestamo

admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Prestamo)
