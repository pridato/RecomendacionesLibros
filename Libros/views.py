from django.shortcuts import render, redirect

from .models import Libro


def listar_libros(request):
    libros = Libro.objects.all()
    print(libros)
    return render(request, 'Libros/listar_libros.html', {'libros': libros})
