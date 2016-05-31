from django import forms
from localflavor.fr.forms import FRPhoneNumberField
from django.contrib.localflavor.br.forms import BRCPFField
form models import Cliente

class Clienteform(forms.ModelForm):
	phone = FRPhoneNumberField()
	

	class Meta:
		model= Cliente
		fields = ['nome','sobrenome','rg']
