from django.db import models

from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cambio = models.CharField(max_length=20)
    cor = models.CharField(max_length=30)
    combustivel = models.CharField(max_length=20)

    def __str__(self):
        return self.placa
