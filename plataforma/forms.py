from django import forms
from .models import Pacientes, Evolucao

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['nome', 'sexo', 'cpf', 'estadocivil', 'datanascimento', 'naturalidade', 'profissao', 'email', 'telefone', 'endereco']
        
        
class EvolucaoForm(forms.ModelForm):
    class Meta:
        model = Evolucao
        fields = ['paciente', 'titulo', 'evolucao']


