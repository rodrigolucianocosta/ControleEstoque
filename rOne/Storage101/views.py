from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
	context = {'texto': 'Projeto Django Linux'}

	return render(request, 'index.html', context)

def current_time(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
