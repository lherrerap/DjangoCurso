from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from applications.home.models import Prueba

# Create your views here.


class IndexView(TemplateView):
    template_name = "home/home.html"


class PruebaView(ListView):
    template_name = "home/lista.html"
    queryset = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    context_object_name = "lista_numeros"



class PruebaListView(ListView):
    model = Prueba
    template_name = "home/lista_prueba.html"
    context_object_name = "lista"

