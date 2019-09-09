from django.forms import ModelForm
from .models import Clientes

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'sobrenome', 'idade', 'salario', 'bio', 'foto']
