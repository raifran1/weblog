from django import forms
from .models import Postagem
from autor.models import Autor


class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'
