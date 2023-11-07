from django import forms
import models


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'imagen']