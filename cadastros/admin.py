from django.contrib import admin
from cadastros import models
# Register your models here.

@admin.register(models.Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'email', 'created_date',
    ordering = '-id',
    list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 25
    list_max_show_all = 200
    list_display_links = 'id', 'first_name',