from django import forms
from .models import Autor, Genero

class AutorForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nacionalidad = forms.CharField(label='Nacionalidad', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    
class LibroForm(forms.Form):
    titulo = forms.CharField(
        label='Título', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    autor = forms.ModelChoiceField(
        label='Autor', queryset=Autor.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})
    )
    fecha_publicacion = forms.DateField(
        label='Fecha de Publicación', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    genero = forms.ModelChoiceField(
        label='Género', queryset=Genero.objects.all(), widget=forms.Select(attrs={'class': 'form-control'})
    )
    
class GeneroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))