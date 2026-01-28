from django.http import HttpResponse
from django.template import loader
from .models import Bruker

def brukere(request):
  mymembers = Bruker.objects.all().values()
  template = loader.get_template('alle_brukere.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def detaljer(request, id):
  mymember = Bruker.objects.get(id=id)
  template = loader.get_template('detaljer.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())