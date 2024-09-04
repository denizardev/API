from django.db import models

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    
    nome_professor = models.CharField(max_length=100)
    numero_sala = models.CharField(max_length=10)
    
    nota_primeiro_semestre = models.DecimalField(max_digits=7, decimal_places=2)  # Atualizado
    nota_segundo_semestre = models.DecimalField(max_digits=7, decimal_places=2)   # Atualizado

    def __str__(self):
        return self.nome
