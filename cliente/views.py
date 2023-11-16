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

from empresarial.models import Empresa
from cinema.models import Bilhete,Cartaz,Sessao
from django.http import HttpResponse, FileResponse





def home( request):
    
    if request.method=='GET':
        cartazes=Cartaz.objects.all()
        for car in cartazes:
            print(car.imagem_cartaz.url)
        return render(request,'home.html',{'cartazes':cartazes})