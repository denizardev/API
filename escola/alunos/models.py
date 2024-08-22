from django.db import models

# Create your models here.
class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    nota_primeiro_semestre = models.FloatField()
    nota_segundo_semestre = models.FloatField()
    nome_professor = models.CharField(max_length=100)
    numero_sala = models.CharField(max_length=10)

    def __str__(self):
        return self.nome