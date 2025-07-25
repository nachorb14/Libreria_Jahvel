from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Autor, Libro, Genero, Biblia
from .forms import AutorForm, LibroForm, GeneroForm, BibliaForm


# Create your views here.
def inicio(request):
    return render(request, 'libreria/inicio.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = Autor(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                nacionalidad=form.cleaned_data['nacionalidad'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
            )
            autor.save()
            return redirect('inicio')
            
    else:
        form = AutorForm()
        return render(request, 'libreria/crear_autor.html', {'form': form})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = Libro(
                titulo=form.cleaned_data['titulo'],
                autor=form.cleaned_data['autor'],
                fecha_publicacion=form.cleaned_data['fecha_publicacion'],
                genero=form.cleaned_data['genero']
            )
            libro.save()
            return redirect('libros')
            
    else:
        form = LibroForm()
        return render(request, 'libreria/crear_libro.html', {'form': form})
    
def crear_genero(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            genero = Genero(nombre=form.cleaned_data['nombre'])
            genero.save()
            return redirect('inicio')
            
    else:
        form = GeneroForm()
        return render(request, 'libreria/crear_genero.html', {'form': form})
    
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libreria/libros.html', {'libros': libros})
    
def buscar_libros(request):
    if request.method == 'GET':
        titulo = request.GET.get('titulo', '')
        libros = Libro.objects.filter(titulo__icontains=titulo)
        return render(request, 'libreria/libros.html', {'libros': libros, 'titulo': titulo})
    
    
#Vistas basadas en clases
class BibliaListView(ListView):
    model = Biblia
    template_name = 'libreria/listar_biblias.html'
    context_object_name = 'biblias'

class BibliaCreateView(CreateView):
    model = Biblia
    form_class = BibliaForm
    template_name = 'libreria/crear_biblia.html'
    success_url = reverse_lazy('listar-biblias')
    
class BibliaDetailView(DetailView):
    model = Biblia
    template_name = 'libreria/detalle_biblia.html'
    context_object_name = 'biblia'
    
class BibliaUpdateView(UpdateView):
    model = Biblia
    form_class = BibliaForm
    template_name = 'libreria/crear_biblia.html'
    success_url = reverse_lazy('listar-biblias')
    
class BibliaDeleteView(DeleteView):
    model = Biblia
    template_name = 'libreria/eliminar_biblia.html'
    success_url = reverse_lazy('listar-biblias')