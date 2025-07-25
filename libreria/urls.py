from django.urls import path
from .views import inicio, crear_autor, crear_libro, crear_genero, buscar_libros, libros, BibliaCreateView, BibliaListView, BibliaDetailView, BibliaUpdateView, BibliaDeleteView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear-autor/', crear_autor, name='crear-autor'),
    path('crear-libro/', crear_libro, name='crear-libro'),
    path('crear-genero/', crear_genero, name='crear-genero'),
    path('libros/', libros, name='libros'),
    path('libros/buscar/', buscar_libros, name='buscar-libros'),
    
    #urls con vistas basadas en clases
    path('crear-biblia/', BibliaCreateView.as_view(), name='crear-biblia'),
    path('listar-biblias/', BibliaListView.as_view(), name='listar-biblias'),
    path('detalle-biblia/<int:pk>', BibliaDetailView.as_view(), name='detalle-biblia'),
    path('editar-biblia/<int:pk>', BibliaUpdateView.as_view(), name='editar-biblia'),
    path('eliminar-biblia/<int:pk>', BibliaDeleteView.as_view(), name='eliminar-biblia')
]
