from django.db import models

from usuarios .models import Users
from empresarial.models import Empresa
from cliente.models import Cliente


class Cinema(models.Model):
    provincia_choices=(('Maputo','Maputo'),
                       ('Gaza','Gaza'),
                       ('Inhambane', 'Inhambane'),
                       ('Sofala', 'Sofala'),
                       ('Manica', 'Manica'),
                       ('Tete', 'Tete'),
                       ('Zambézia', 'Zambézia'),
                       ('Nampula', 'Nampula'),
                       ('Cabo Delgado', 'Cabo Delgado'),
                       ('Niassa', 'Niassa'),)
    
    nome=models.CharField(max_length=80)
    estado=models.BooleanField(default=False)
    capacidade_lotacao=models.IntegerField()
    provincia=models.CharField(max_length=15,choices=provincia_choices)
    distrito=models.CharField(max_length=40)
    bairro=models.CharField(max_length=40)
    
    usuario=models.ForeignKey(Users, on_delete=models.SET_NULL, null=True,blank=True)
    empresa=models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True,blank=True)
    create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
    updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
    
    def __str__(self):
      return  self.nome

class Actor (models.Model):
  nome=models.CharField(max_length=80)
  nacionalidade=models.CharField(max_length=80)
  data_nascimento=models.DateField()
  
  create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
  updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
  
  
  class Meta:
    verbose_name_plural="Autores"
  
  def __str__(self):
      return  self.nome 
    
    
class Director(models.Model):
  nome=models.CharField(max_length=80)
  nacionalidade=models.CharField(max_length=80)
  data_nascimento=models.DateField()
  
  
  create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
  updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
  
  
  class Meta:
    verbose_name_plural="Directores"
  
  
  def __str__(self):
      return  self.nome 
    
  
  
  
class Filme(models.Model):
  titulo=models.CharField(max_length=120)
  genero=models.CharField(max_length=80)
  origem=models.CharField(max_length=80)
  duracao=models.TimeField()
  cinema=models.ForeignKey(Cinema, on_delete=models.SET_NULL, null=True,blank=True)
  actor=models.ManyToManyField(Actor,blank=True)
  director=models.ForeignKey(Director, on_delete=models.SET_NULL, null=True,blank=True)
  capa=models.ImageField(upload_to='Capa_Filme')
  
  create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
  updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
  
  def __str__(self):
      return  self.titulo +"_"+self.genero +"_"+str(self.duracao)
  
  
  

class Cartaz(models.Model):
  
  filme=models.ManyToManyField(Filme,blank=True)
  molde=models.ImageField(upload_to='molde_cartaz',null=True,blank=True)
  imagem_cartaz=models.ImageField(upload_to='Imagem_cartaz',null=True,blank=True)
  cinema=models.ForeignKey(Cinema, on_delete=models.SET_NULL, null=True,blank=True)
  

  create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
  updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
  
  class Meta:
    verbose_name_plural="Cartazes"
  
  def __str__(self):
     
      return str(Cartaz.pk)+"_"+self.cinema.nome
    


class Sessao(models.Model):
  data=models.DateField()
  inicio=models.TimeField()
  fim=models.TimeField()
  publico=models.IntegerField()
  create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
  updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
  cinema=models.ForeignKey(Cinema, on_delete=models.SET_NULL, null=True,blank=True)
  
  
  def __str__(self):
      return  str(self.inicio )+"---"+str(self.fim) +"_"+str(self.data)
    
    

  

class Bilhete(models.Model):
  quantidade=models.IntegerField()
  preco=models.FloatField()
  sessao=models.ForeignKey(Sessao,on_delete=models.SET_NULL, null=True,blank=True)
  filme=models.ForeignKey(Filme,on_delete=models.SET_NULL, null=True,blank=True)
  cinema=models.ForeignKey(Cinema,on_delete=models.SET_NULL, null=True,blank=True)
  
  
  create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
  updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
  
  
  def __str__(self):
      return  str(self.filme.titulo)+"_"+str(self.sessao.inicio)+"---"+str(self.sessao.fim)+"_"+self.cinema.nome 
  
  
class solicitacao(models.Model):
   cliente=models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True,blank=True)
   status=models.BooleanField()
   bilhete=models.ForeignKey(Bilhete, on_delete=models.SET_NULL, null=True,blank=True)
   
   create_at=models.DateTimeField( verbose_name='Data_criação',auto_now_add=True)
   updated_at=models.DateTimeField( verbose_name='Data_atualização',auto_now=True)
   
   
   def __str__(self):
      return  str(self.bilhete.filme.titulo)+"_"+str(self.cliente.nome)+"_"+str(self.bilhete.sessao.inicio)+"---"+str(self.bilhete.sessao.fim)
   