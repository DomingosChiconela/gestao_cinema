
from django.urls import path
from.import views
urlpatterns = [
    path('cadastro_cliente/',views.cadastro_cliente, name="cadastro_cliente"),
      path('cadastro_empresa/',views.cadastro_empresa, name="cadastro_empresa"),
    
    path('login/',views.login, name="login"),
    path('sair/',views.logout, name="sair"),
    
]