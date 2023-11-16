
from django.urls import path
from.import views
urlpatterns = [
    path('dasboar_empresa/',views.dasboar_empresa, name="dasboar_empresa"),
    path('empresa_cadastro_cinema/',views.empresa_cadastro_cinema, name="empresa_cadastro_cinema"),
    path('empresa_view_cinema/',views.empresa_view_cinema, name="empresa_view_cinema"),
    path('editar_cinema/<int:id>/',views.editar_cinema, name="editar_cinema"),
    
    path('detalhes_cinema/<int:id>/',views.detalhes_cinema, name="detalhes_cinema"),
        path('eliminar_cinema/<int:id>/',views.eliminar_cinema, name="eliminar_cinema"),
    
    
    ]
