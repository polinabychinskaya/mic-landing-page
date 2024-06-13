from django.shortcuts import render
from django.views import generic

# Create your views here.
class Magvit(generic.TemplateView):
    template_name = 'magvit.html'

class Validol(generic.TemplateView):
    template_name = 'validol.html'