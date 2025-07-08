from django.contrib import admin

# Register your models here.
from .models import Autor, Libro, Genero

register_models = [Autor, Libro, Genero]

admin.site.register(register_models)