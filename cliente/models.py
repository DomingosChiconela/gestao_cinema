from django.db import models


class Cliente (models.Model):
  nome=models.CharField(max_length=80)
  data_nascimento=models.DateField()
  
  create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
  updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
  
  def __str__(self):
      return  self.nome 