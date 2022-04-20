#========|
# Imports|
#========|

# Typing
import json
from typing import (
    Any,
    ByteString,
    Literal,
    Iterable,
)
from django.http import HttpResponse
from django.shortcuts import render

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
    template_name = ""

    # NOTE: To obtain request data, we depend from HTTP method:
    # GET METHOD: request.GET['any']   || request.GET.get('any')
    # POST METHOD: request.POST['any'] || request.POST.get('any')
    # POST METHOD: request.data['any'] || request.data.get('any')
    def get_context_data(self, **kwargs):
        
        return super().get_context_data(**kwargs)
    
# Create sale
class CreateRecordSale(CreateView):

    # My model
    model = ModelSales
    form_class = forms.FormSales
    # For indicate the form
    template_name = 'sales/sales_register.html'
    template_name_suffix = '_form'
    # If save successful, redirec to:
    success_url = 'http://localhost:8000/tiendalissa/crear-ventas/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = ModelSales.objects.all()
        context['form'] = self.form_class
        return context

    # Post form
    def post(self,request):
        
        # save one record at a time
        if request.method == "POST":
            form = self.form_class(request.POST)

            if form.is_valid():
                
                form.save()
                return render(request,self.template_name,{'form':form})
        # If form is invalid, return form
        return render(request,self.template_name,{'form':form})
        
class UpdateRecordSale(UpdateView):
    pass