from django.urls import path
from .views import inicio, crear_autor, crear_libro, crear_genero, buscar_libros, libros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-autor/', crear_autor, name='crear_autor'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path('crear-genero/', crear_genero, name='crear_genero'),
    path('libros/', libros, name='libros'),
    path('libros/buscar/', buscar_libros, name='buscar_libros'),
]
