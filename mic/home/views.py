from django.shortcuts import render
from django.views import generic
from . import models
from  django.urls import reverse_lazy

# Create your views here.
class HomePage(generic.ListView):
    template_name = 'home.html'
    model = models.Article

class ArticleView(generic.DetailView):
    model = models.Article
    template_name='article.html'