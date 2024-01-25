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
from rolepermissions.decorators import has_permission_decorator
from empresarial.models import Empresa
from cinema.models import Bilhete,Cartaz,Sessao,Filme
from django.http import HttpResponse, FileResponse




@login_required
@has_permission_decorator('Visualizar_cartaz')
def home( request):
    
    if request.method=='GET':
        cartazes=Cartaz.objects.all()
        filmes=Filme.objects.all()
        return render(request,'home.html',{'cartazes':cartazes,'filmes':filmes})