import random
from random import  choice, shuffle
import string
from django.conf import settings
from django.template.loader import render_to_string
from io import BytesIO
from weasyprint import HTML,images
import os
from datetime import date





def gerar_senha_aleatoria(tamanho):

    caracteres_especiais = string.punctuation   
    caracteres = string.ascii_letters
    numeros_list = string.digits

    
    sobra = 0
    qtd = tamanho // 3
    if not tamanho % 3 == 0:
        sobra = tamanho - qtd

    letras = ''
    for i in range(0, qtd + sobra):
        letras += choice(caracteres)

    numeros = ''
    for i in range(0, qtd):
        numeros += choice(numeros_list)

    especiais = ''
    for i in range(0, qtd):
        especiais += choice(caracteres_especiais)

    
    senha = list(letras + numeros + especiais)
    shuffle(senha)

    return ''.join(senha)



def gerar_pdf_cadastro_cinema(senha,usuario,email,nome,capacidade_lotacao,provincia,distrito,bairro):
    data_hoje=date.today().strftime('%d/%m/%Y')
#onde deve ser procurado o arquivo html
    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/info_cadastro_cinema.html')

    
    #apos achar , sendo renderizado
    template_render = render_to_string(path_template, {'senha':senha,'usuario':usuario,'email':email,'nome':nome,'capacidade_lotacao':capacidade_lotacao,'provincia':provincia,'distrito':distrito,'bairro':bairro,'data_hoje':data_hoje})
    
#instaciando a classe para bytesio para salvar em menoria(ram)
    path_output = BytesIO()
    
#escrevendo ou transformando o html em pdf e passando o caminho onde deve ser salvo
    HTML(string=template_render).write_pdf(path_output)
    
    #indicando o ponteiro ou o indice em que deve iniciar aleitura do ficheiro
    path_output.seek(0)
    
    return path_output
        