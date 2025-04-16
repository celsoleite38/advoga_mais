from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from pacientes.models import Category
# Create your views here.

def index(request):
    return HttpResponse('Ola, django-index')

def pacientes(request):
    return HttpResponse('Ola, django')

class CreateCategoryView(CreateView):
    model = Category
   # form_class = CategoryForm
    fields = ('Name', 'description')
    template_name ='create_category.html'
    success_url = reverse_lazy('create_category')