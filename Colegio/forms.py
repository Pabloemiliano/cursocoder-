from django import forms


class BuscarCursoform(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

