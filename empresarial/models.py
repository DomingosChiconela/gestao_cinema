from django.db import models
from usuarios .models import Users


class Empresa(models.Model):
    usuario=models.ForeignKey(Users, on_delete=models.SET_NULL, null=True,blank=True)
    nome=models.CharField(max_length=80)
    create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
    updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
    
    def __str__(self):
      return  self.nome