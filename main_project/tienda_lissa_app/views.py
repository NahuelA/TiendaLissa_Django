#========|
# Imports|
#========|

# Typing
import json
from re import M
from typing import (
    Any,
    ByteString,
    Literal,
    Iterable,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

# Local models
from tienda_lissa_app.models import ModelSales

# Local forms
from tienda_lissa_app import forms

from django.views.generic.list import ListView
# Generic edit
from django.views.generic.edit import (

    FormView,
    CreateView,
    UpdateView,
    DeleteView
)


# Generic views
from django.views.generic.base import (

    # TemplateView and RedirectView inherit View class
    TemplateView, RedirectView
)

# Libraries of thirds
import datetime

#========================|
# Create your views here.|
#========================|


# CRUD to model

#**************|
# Create sales:|
#**************|

class ReadSales(ListView):
    model = ModelSales
    template_name = "index.html"

    # NOTE: To obtain request data, we depend from HTTP method:
    # GET METHOD: request.GET['any']   || request.GET.get('any')
    # POST METHOD: request.POST['any'] || request.POST.get('any')
    # POST METHOD: request.data['any'] || request.data.get('any')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = ModelSales.objects.all()
        return context
    
""" Create record """
class CreateRecordSale(CreateView):

    # My model
    model = ModelSales
    form_class = forms.FormSales
    # For indicate the form
    template_name = 'sales/sales_register.html'
    # If save successful, redirec to:
    success_url = reverse_lazy('create-ventas')


""" Delete record """    
class DeleteRecordSale(DeleteView):
    model = ModelSales
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = ModelSales.objects.get(id=self.object.id)
        return context
    
""" Update record """
class UpdateRecordSale(UpdateView):
    model = ModelSales
    fields = ['name','description','count','price','paid_out']
    template_name = 'update.html'
    success_url = reverse_lazy('home')