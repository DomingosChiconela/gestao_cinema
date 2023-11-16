from rolepermissions.roles import AbstractUserRole






class Empresa(AbstractUserRole):
    available_permissions= {
        'cadastrar_cinema':True,
        'Editar_cinema':True,
        'Eliminar_eliminar':True,
        'Visualizar_numero_cinemas':True,
        'Visualizar_numero_BI_Total':True,
        'Visualizar_numero_BI_Erro_Total':True,
         'view_home_empresa':True,
         'CRUD_perfil_empresa':True,
        
        
        
        
    }
    
    

class Cinema(AbstractUserRole):
    available_permissions= {
        'cadastrar_filme':True,
        'Editar_filme':True,
        'Eliminar_filme':True,
        'Visualizar_filme':True,
        
        'cadastrar_cartaz':True,
        'Editar_cartaz':True,
        'Eliminar_cartaz':True,
        'Visualizar_cartaz':True,
        
         'cadastrar_sessao':True,
        'Editar_sessao':True,
        'Eliminar_sessao':True,
        'Visualizar_sessao':True,
        
        
        'criar_bilhete':True,
        'Editar_bilhete':True,
        'Eliminar_bilhete':True,
        'Visualizar_bilhete':True,
        
        
        'CRUD_perfil_cinema':True,
        'view_home_cinema':True,
        
        
        
        
    }
    
    
    
    
class Cliente(AbstractUserRole):
    available_permissions= {
        'Visualizar_cartaz':True,
        'Comprar_bilhete':True,
      
        'Visualizar_filme':True,
        
        
        
        
        
        
    }
    


class Admi(AbstractUserRole):
    available_permissions= {
          'cadastrar_empresa':True,
        'Editar_empresa':True,
        'Eliminar_empresa':True,
        'Visualizar_empresa':True,
        
        
       'cadastrar_filme':True,
        'Editar_filme':True,
        'Eliminar_filme':True,
        'Visualizar_filme':True,
        
        'cadastrar_cartaz':True,
        'Editar_cartaz':True,
        'Eliminar_cartaz':True,
        'Visualizar_cartaz':True,
        
         'cadastrar_sessao':True,
        'Editar_sessao':True,
        'Eliminar_sessao':True,
        'Visualizar_sessao':True,
        
        
        'criar_bilhete':True,
        'Editar_bilhete':True,
        'Eliminar_bilhete':True,
        'Visualizar_bilhete':True,
        
        
        'CRUD_perfil_cinema':True,
        'view_home_cinema':True,
        
         'cadastrar_cinema':True,
        'Editar_cinema':True,
        'Eliminar_eliminar':True,
        'Visualizar_numero_cinemas':True,
        'Visualizar_numero_BI_Total':True,
        'Visualizar_numero_BI_Erro_Total':True,
         'view_home_empresa':True,
         'CRUD_perfil_empresa':True,
        
        
        
    }