from django.db import models

# Create your models here.
class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    
    
    nome_professor = models.CharField(max_length=100)
    numero_sala = models.CharField(max_length=10)
     
    nota_primeiro_semestre = models.DecimalField(max_digits=5, decimal_places=2)
    nota_segundo_semestre = models.DecimalField(max_digits=5, decimal_places=2)
    professor = models.CharField(max_length=100)
    sala = models.CharField(max_length=20)

    def __str__(self):
        return self.nome