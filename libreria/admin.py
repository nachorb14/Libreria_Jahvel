from django.contrib import admin

# Register your models here.
from .models import Autor, Libro, Genero, Biblia

register_models = [Autor, Libro, Genero, Biblia]

admin.site.register(register_models)