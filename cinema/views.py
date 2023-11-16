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
from .models import Cinema,Actor,Director,Bilhete,Cartaz,Filme,Sessao
from empresarial.models import Empresa
from PIL import  Image,ImageFont,ImageDraw
from django.http import HttpResponse, FileResponse
import os 
from django.conf import settings
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile,TemporaryUploadedFile,SimpleUploadedFile
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime,date





def dasboar_cinema( request):
    cinema_id_do_usuario = Cinema.objects.filter(usuario=request.user).values_list('id', flat=True).first()
    
    if request.method=='GET':
        
        cartazes =Cartaz.objects.filter(cinema=cinema_id_do_usuario)
    
        if request.method=='GET':
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
                  
                  
            total_cartaz=Cartaz.objects.filter(cinema=cinema_id_do_usuario).count()
            total_filme=Filme.objects.filter(cinema=cinema_id_do_usuario).count()
            total_sessao=Sessao.objects.filter(cinema=cinema_id_do_usuario).count()
                  
        return render(request,'dasboar_cinema.html',{'labels': list(Cartazes.keys()), 'values': list(Cartazes.values()),'total_cartaz':total_cartaz,'total_filme':total_filme, ' total_sessao': total_sessao})
    
    
    
    
def view_perfil_cinema(request):
    cinema_id_do_usuario = Cinema.objects.filter(usuario=request.user).values_list('id', flat=True).first()
    
    if request.method=='GET':
        cinema=Cinema.objects.get(id=cinema_id_do_usuario)
        
        return render(request,'view_perfil_cinema.html',{'cinema':cinema})
    
    
def view_filme(request):
    cinema_id_do_usuario = Cinema.objects.filter(usuario=request.user).values_list('id', flat=True).first()
    if request.method=='GET':
        filmes=Filme.objects.filter(cinema=cinema_id_do_usuario)
        
        return render(request,'view_filme.html',{'filmes':filmes})
    



def view_cartaz(request):
    cinema_id_do_usuario = Cinema.objects.filter(usuario=request.user).values_list('id', flat=True).first()
    if request.method=='GET':
        cartazes=Cartaz.objects.filter(cinema=cinema_id_do_usuario)
        
        return render(request,'view_cartaz.html',{'cartazes':cartazes})
    





def cadastrar_filme(request):
    
    
    if request.method=="GET":
        atores=Actor.objects.all()
        directores=Director.objects.all()
        
        
        return render(request,'cadastrar_filme.html',{'atores':atores,'directores':directores})
    
    elif request.method=="POST":
        
        titulo=request.POST.get('titulo')
        duracao=request.POST.get('duracao')
        genero=request.POST.get('genero')
        origem=request.POST.get('origem')
        director=request.POST.get('director')
        atore= request.POST.getlist('atores')
        capa=request.FILES.get('capa')
        
        
        titulo=str(titulo).strip()
        duracao=str(duracao).strip()
        genero=str( genero).strip()
        origem=str(origem).strip()
        
        
    if not  titulo and not  duracao and not genero and not director and not atore  and not capa :
        
        messages.add_message(request, constants.ERROR, 'Preecha todos os campos do formulario ')  
        return redirect(reverse('cadastrar_filme'))
    
    else:
        cinema_id_do_usuario = Cinema.objects.filter(usuario=request.user).values_list('id', flat=True).first()
        filme=Filme( titulo=titulo,
                    genero=genero,
                    origem=origem,
                    duracao=duracao,
                    cinema_id=cinema_id_do_usuario,
                    
                    director_id=director,
                    capa=capa, 
            
        )
        filme.save()
        filme.actor.set(atore)
        filme.save()
        messages.add_message(request, constants.SUCCESS, 'Filme registado com sucesso  ')  
        return redirect(reverse('view_filme'))
    
    
    


def cadastrar_cartaz(request):
    cinema_id_do_usuario = Cinema.objects.filter(usuario=request.user).values_list('id', flat=True).first() 
    if request.method=="GET":
       
        filmes=Filme.objects.filter(cinema=cinema_id_do_usuario )
        
        
        return render(request,'cadastrar_cartaz.html',{'filmes':filmes}) 
    
    elif request.method=="POST":
        filmes= request.POST.getlist('filmes')
        molde=request.FILES.get('molde')
        
        
        if not filmes and not molde:
            messages.add_message(request, constants.ERROR, 'Preecha todos os campos do formulario ')  
            return redirect(reverse('cadastrar_cartaz'))
        
        else:
            cartaz=Cartaz( 
                            molde=molde,
                            cinema_id=cinema_id_do_usuario   
                
            )
            cartaz.save()
            cartaz.filme.set(filmes)
            cartaz.save()
            
           
            #pegando id de cada capa de filme
            filme=Filme.objects.get(id=filmes[0])
            if len(filmes)>1:
               filme2=Filme.objects.get(id=filmes[1]) 
            if len(filmes)>2:
                filme3=Filme.objects.get(id=filmes[2]) 
                
            #caminhos para imagens
            raiz_dir=os.path.join(settings.BASE_DIR,' ')
            caminho_molde=raiz_dir[:len(raiz_dir)-2]+str(cartaz.molde.url)
            
            caminho_filme=raiz_dir[:len(raiz_dir)-2]+str(filme.capa.url)
            if len(filmes)>1:
                caminho_filme2=raiz_dir[:len(raiz_dir)-2]+str(filme2.capa.url)
            if len(filmes)>2:
                caminho_filme3=raiz_dir[:len(raiz_dir)-2]+str(filme3.capa.url)
                
                
            #abrindo as imagens
            img=Image.open(caminho_filme)
            molde_base=Image.open(caminho_molde)
            if len(filmes)>1:
                img2=Image.open(caminho_filme2)
            if len(filmes)>2:
                img3=Image.open(caminho_filme3)
           
            
            
            #redirecionamento
            tamanho=(953,689)
            img.thumbnail(tamanho)
            if len(filmes)>1:
                tamanho2=(949,749)
                img2.thumbnail(tamanho2)
                
            if len(filmes)>2:
                tamanho3=(961,737)
                img3.thumbnail(tamanho3)
            
            #posicao onde deve ficar a imagem do bi(foto_bi)
            posicao_insercao = (509, 45) 
            posicao_insercao2 = (61,741) 
            posicao_insercao3 = (1101,7851) 
            
            

            # Cole a imagem inserida na imagem principal
            molde_base.paste(img, posicao_insercao)
            if len(filmes)>1:
                molde_base.paste(img2, posicao_insercao2)
            if len(filmes)>2:
                molde_base.paste(img3, posicao_insercao3)
                   
            #colocando de ram
            
            output = BytesIO()
            molde_base.save(output, format="PNG", quality=100)
            output.seek(0)
            imagem_cartaz= InMemoryUploadedFile(output,
                                          'ImageField',
                                          f'Cartaz.png',
                                          'image/jpg',
                                          sys.getsizeof(output),
                                          None)
            
            cartaz.imagem_cartaz=imagem_cartaz
            cartaz.save()
            
            messages.add_message(request, constants.SUCCESS, 'Cartaz registado com sucesso  ')  
            return redirect(reverse('view_cartaz'))
 
            
            
        
            
       
    
        
         
    

    
    