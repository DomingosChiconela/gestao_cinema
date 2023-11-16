from django.dispatch import receiver
from django.db.models.signals import post_save

from. models import Users
from rolepermissions.roles import assign_role


@receiver(post_save, sender=Users)
def define_permissoes(sender,instance,created, ** kwargs):
    if created:
        if instance.status =="A":
            assign_role(instance,'admi')
            print("admi")
        if instance.status =="E":
            assign_role(instance,'empresa')
            print("empresa")
        if instance.status =="Ci":
            assign_role(instance,'cinema')
            print("cinema")
        if instance.status =="C":
            assign_role(instance,'cliente')
            print("cliente")