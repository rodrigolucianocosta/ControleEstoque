from django.contrib import admin

# Register your models here.
from .models import Cliente
from .models import Endereco

class clienteAdmin(admin.ModelAdmin):
	list_display = ['nome','sobrenome','email','rg']

#class enderecoAdmin(admin.ModelAdmin):
#	list_display = ['rua','numero','bairro','cidade','cep','estado']

admin.site.register(Cliente, clienteAdmin)
#admin.site.register(Endereco, enderecoAdmin)
