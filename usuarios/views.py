from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth 
from .models import Users
import re
from django.contrib.auth.decorators import login_required



def cadastro_cliente(request):
    if request.method=='GET':
        
        return render(request,'cadastro_cliente.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        senha =request.POST.get('senha')
        confirmar_senha=request.POST.get('confirmar_senha')
        
    
    
    if not senha==confirmar_senha:
           
           messages.add_message(request,constants.ERROR, 'As senha não coincidem.')
           return redirect(reverse('cadastro_cliente'))
       
       
    if len(senha)<8:
        messages.add_message(request, constants.ERROR, 'A senha deve ter pelo menos 8 caracteres.')
        return redirect(reverse('cadastro_cliente'))
    
    
    user= Users.objects.filter(username=username)
    if user.exists():
        messages.add_message(request,constants.ERROR, 'O usuario ja existes.')
        return redirect(reverse('cadastro_cliente'))
    
    # Cria o usuário
    user=Users.objects.create_user(username=username, email=email, password=senha, status="C" )
    messages.add_message(request,constants.SUCCESS, 'Usuario salvo com sucesso.')
    return  redirect(reverse('login'))


def cadastro_empresa(request):
    if request.method=='GET':
        
        return render(request,'cadastro_cliente.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        senha =request.POST.get('senha')
        confirmar_senha=request.POST.get('confirmar_senha')
        
    
    
    if not senha==confirmar_senha:
           
           messages.add_message(request,constants.ERROR, 'As senha não coincidem.')
           return redirect(reverse('cadastro_empresa'))
       
       
    if len(senha)<8:
        messages.add_message(request, constants.ERROR, 'A senha deve ter pelo menos 8 caracteres.')
        return redirect(reverse('cadastro_empresa'))
    
    
    user= Users.objects.filter(username=username)
    if user.exists():
        messages.add_message(request,constants.ERROR, 'O usuario ja existes.')
        return redirect(reverse('cadastro_empresa'))
    
    # Cria o usuário
    user=Users.objects.create_user(username=username, email=email, password=senha, status="E" )
    messages.add_message(request,constants.SUCCESS, 'Usuario salvo com sucesso.')
    return  redirect(reverse('login'))




def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    
    
    elif request.method=="POST":
       username=request.POST.get('username')
       senha=request.POST.get('senha')
       
       user=auth.authenticate(username=username, password=senha)
       if not user:
           messages.add_message(request, constants.ERROR, 'Username ou senha invalida')
           return redirect(reverse('login'))
       
       auth.login(request,user)
       if user.status=="C":
            return  redirect(reverse('home'))
        
       if user.status=="E":
          return  redirect(reverse('dasboar_empresa'))
           
       if user.status=="P":
           return  redirect(reverse('posto_dasboard'))
       
       if user.status=="Ci":
           return  redirect(reverse('dasboar_cinema'))   
             
       elif user.status=="A":
           HttpResponse("admi")
           
@login_required          
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))
