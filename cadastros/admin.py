from django.contrib import admin
from cadastros import models
# Register your models here.

@admin.register(models.Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'email', 'created_date',
    ordering = '-id',