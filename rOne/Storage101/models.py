from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Cliente(models.Model):
	nome = models.CharField('nome',max_length=100)
	sobrenome = models.CharField('sobrenome',max_length=100,null=True)
	email = models.EmailField('email',max_length=50,null=True)
#	data_nascimento = models.DateTime('data nascimento') //verificar formatos de data
#	cpf = models.IntegerField('cpf')
#	cnpj = BRCNPJField(null=True,blank=True)
	rg = models.CharField(max_length=20)
	
#	def __unicode__(self):
#		return u"cpf: %s ,cnpj: %s" % (self.cpf or u", self.cnpj or u")
	class Meta:
		verbose_name = "cliente"
		verbose_name = "clientes"

	def __unicode__(self):
		return u"%s %s %s %s"%(self.nome,self.sobrenome,self.email,self.rg)
	
class Endereco(models.Model):
	rua = models.CharField(max_length=100)
	numero = models.IntegerField(default=0)
	bairro = models.CharField(max_length=100)
	cep = models.CharField(max_length=100)
	cidade = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)

