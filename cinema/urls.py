
from django.urls import path
from . import views


urlpatterns = [
    
            path('dasboar_cinema/',views.dasboar_cinema, name="dasboar_cinema"),
            path('view_perfil_cinema/',views.view_perfil_cinema, name="view_perfil_cinema"),
            path('view_filme/',views.view_filme, name="view_filme"),
             
            path('cadastrar_filme/',views.cadastrar_filme, name="cadastrar_filme"),
            path('cadastrar_cartaz/',views.cadastrar_cartaz, name="cadastrar_cartaz"),
            path('view_cartaz/',views.view_cartaz, name="view_cartaz"),
            
            
          
            
    
]