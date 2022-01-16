from django.db import models
from empresas.models import Empresa

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    chefeDepart = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome