from django.http import HttpResponse
from django.template import loader

def brukere(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())