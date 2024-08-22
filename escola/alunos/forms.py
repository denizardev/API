from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'nota_primeiro_semestre', 'nota_segundo_semestre', 'nome_professor', 'numero_sala']
