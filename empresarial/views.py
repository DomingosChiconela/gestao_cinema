from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth 
import re
from django.contrib.auth.decorators import login_required
from usuarios.models import Users
from cinema.models import Cinema,Cartaz,Bilhete,Sessao,Filme
from.models import Empresa
from.utils import gerar_senha_aleatoria,gerar_pdf_cadastro_cinema
from django.http import HttpResponse, FileResponse
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime,date


@login_required
def dasboar_empresa( request):
    empresa_id_do_usuario = Empresa.objects.filter(usuario=request.user).values_list('id', flat=True).first()
    if request.method=='GET':
        
        cartazes =Cartaz.objects.all()
    
       
        ano_atual = datetime.now().year
        cartazes_ano_atual = cartazes.filter(create_at__year=ano_atual)

        # Agregar dados por mês e ano
        cartazes_agregados =cartazes_ano_atual.annotate(
            mes_ano=TruncMonth('create_at')
            ).values('mes_ano').annotate(
                  total=Count('id')
            )

        # Criar um dicionário com meses e valores totais
        Cartazes= {}
        for item in  cartazes_agregados:
                  mes_ano = item['mes_ano'].strftime('%b %Y')
                  total = item['total']
                  Cartazes[mes_ano] = total  
                  
        total_cinema=Cinema.objects.filter(empresa=empresa_id_do_usuario).count()        
        total_cartaz=Cartaz.objects.all().count()
        total_filme=Filme.objects.all().count()
        total_sessao=Sessao.objects.all().count()
                  
        return render(request,'dasboar_empresa.html', {'total_cinema':total_cinema,'total_cartaz':total_cartaz,'total_filme':total_filme, ' total_sessao': total_sessao})
    
def empresa_view_cinema(request ):
      
      if request.method=='GET':
            cinemas=Cinema.objects.all()
            
            return render(request,'empresa_view_cinema.html',{'cinemas':cinemas})    
      
    
def empresa_cadastro_cinema(request):
      empresa_id_do_usuario = Empresa.objects.filter(usuario=request.user).values_list('id', flat=True).first()
      if request.method=="GET":
            
            
            return render(request,'empresa_cadastro_cinema.html')
      
      elif request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            capacidade_lotacao=request.POST.get('capacidade_lotacao')
            nome_cinema=request.POST.get('nome')
            provincia=request.POST.get('provincia')
            distrito=request.POST.get('distrito')
            bairro=request.POST.get('bairro')
            
            
            senha=gerar_senha_aleatoria(8)
           
            
           
            
             
            user= Users.objects.filter(username=username)
            if user.exists():
                  messages.add_message(request,constants.ERROR, 'O usuario ja existe.')
                  return redirect(reverse('empresa_cadastro_cinema'))
            
          
            
            # Cria o usuário
            user=Users.objects.create_user(username=username, email=email, password=senha, status="Ci" )
            messages.add_message(request,constants.SUCCESS, 'Usuario salvo com sucesso.')
            
            cinema=Cinema(usuario_id=user.id,
                            empresa_id=empresa_id_do_usuario ,
                             nome=nome_cinema,
                             capacidade_lotacao=capacidade_lotacao,
                             distrito=distrito,
                             provincia=provincia,
                             bairro=bairro,)
            cinema.save() 
            
            return FileResponse(gerar_pdf_cadastro_cinema(senha,user.username,user.email,cinema.nome, cinema.capacidade_lotacao,cinema.provincia, cinema.distrito,cinema.bairro), filename=f"info_cadastro_cinema_{nome_cinema}.pdf")
    
    
def editar_cinema(request,id):
     
    cinema=Cinema.objects.get(id=id)
    if request.method=='GET':
       
        
        
        return render(request, 'editar_cinema.html',{'cinema':cinema} )
    
   
    elif request.method=='POST':
         
            capacidade_lotacao=request.POST.get('capacidade_lotacao')
            nome_cinema=request.POST.get('nome')
            provincia=request.POST.get('provincia')
            distrito=request.POST.get('distrito')
            bairro=request.POST.get('bairro')
    
    
        
            nome_cinema = str(nome_cinema).strip()
            provincia= str(provincia).strip()
            distrito= str(distrito).strip()
            bairro = str(bairro).strip()
           
            
            if not nome_cinema and not provincia and  not distrito and not bairro:
                
                messages.add_message(request, constants.ERROR, 'Preecha o formulario para poder editar')
                
                return redirect(reverse('editar_cinema', kwargs={'id':id}))
               
            
            
            else:
                
                print(nome_cinema)
                print(provincia)
                print(distrito)
                print(bairro)
            
                
                cinema.nome = nome_cinema
                cinema.provincia= provincia
                cinema.distrito= distrito
                cinema.bairro= bairro
                cinema.capacidade_lotacao= capacidade_lotacao
                cinema.save()
                
                
                messages.add_message(request, constants.SUCCESS, 'Edição efetuada com sucesso')
                  
                return redirect(reverse('empresa_view_cinema'))
            
            
            
            
def detalhes_cinema(request,id):
     
    cinema=Cinema.objects.get(id=id)
    if request.method=='GET':
       
        
        
        return render(request, 'detalhes_cinema.html',{'cinema':cinema} )
                
                
                
            
def eliminar_cinema(request,id):
     
    cinema=Cinema.objects.get(id=id)
    cinema.delete()
        
    return redirect(reverse('empresa_view_cinema'))
                
                
                
                
                
                
                
                
                
                
                
                
                