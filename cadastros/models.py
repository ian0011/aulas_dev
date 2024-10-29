from django.db import models
from django.utils import timezone
# Create your models here.

class Cadastro (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    #Alterando o nome Exibido na lista de usuários
    def __str__(self):
        return f'{self.first_name} {self.last_name}'