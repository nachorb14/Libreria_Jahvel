from django.shortcuts import render, redirect
from .models import Autor, Libro, Genero
from .forms import AutorForm, LibroForm, GeneroForm


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
            return redirect('inicio')
            
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