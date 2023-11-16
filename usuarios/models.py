from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    choices_status=(('A', 'Admi'),
                    ('E','Empresa'),
                   ('Ci','Cinema'),
                   ('C','Cliente'))
    
    
    status=models.CharField(max_length=28, choices=choices_status)