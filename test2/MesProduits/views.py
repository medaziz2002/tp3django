from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from MesProduits.models import Produits
from django.urls import reverse
def index(request):
    prod = Produits.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'prod': prod,
    }
    return HttpResponse(template.render(context, request))
def del_prod(request, id):
    produits = Produits.objects.get(id=id)
    produits.delete()
    return HttpResponseRedirect(reverse('index'))
