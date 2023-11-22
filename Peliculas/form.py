from django import forms

class PeliculaForm(forms.Form):
    titulo = forms.CharField()
    director = forms.CharField()
    genero = forms.CharField()