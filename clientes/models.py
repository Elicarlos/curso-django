from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=6, decimal_places=2)
    bio = models.TextField()
    foto =  models.ImageField(upload_to='media/fotos_clientes', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome