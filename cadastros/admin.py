from django.contrib import admin
from cadastros import models
# Register your models here.

@admin.register(models.Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    ...