from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
	return HttpResponse("Hello, word")

def current_time(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
