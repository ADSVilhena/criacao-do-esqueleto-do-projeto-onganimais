from django import forms

class cadastroAnimal(forms.Form):
    name = forms.CharField(labelNome:'Nome', max_length=100)