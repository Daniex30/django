from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView,DeleteView
from applications import servicio_tipos

from applications.servicio_tipos.models import Servicio_tipo

from .models import Servicio_tipo
from .forms import ServicioForm
# Create your views here.
class ListServicioTipo(ListView):
    template_name = "servicio_tipos/index.html"
    model = Servicio_tipo
    context_object_name = 'lista'

class DetailServicioTIpo(DetailView):
    model = Servicio_tipo
    template_name = "servicio_tipos/detail.html"

class CreateServicioTipo(CreateView):
    model = Servicio_tipo
    template_name = 'servicio_tipos/add.html'
    form_class = ServicioForm
    success_url = '/'

class UpdateServicioTipo(UpdateView):
    model = Servicio_tipo
    template_name = "servicio_tipos/update.html"
    fields = ['name']
    success_url = '/'

class DeleteServicioTipo(DeleteView):
    model = Servicio_tipo
    template_name = "servicio_tipos/delete.html"
    success_url = "/"
   