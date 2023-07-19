from django.forms import ModelForm
from django import forms
from produto.models import Marca

class MarcaForm(ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'logo' : forms.FileInput(attrs={'class': 'form-control' }),
        }