from rest_framework import serializers
from .models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'idade', 'nota_primeiro_semestre', 'nota_segundo_semestre', 'professor', 'sala']
