#========|
# Imports|
#========|

# Typing
from typing import (
    Any,
    ByteString,
    Literal,
    Iterable,
)
from django.http import HttpResponse

# For render templates context
from django.shortcuts import render
from django.template import loader

# For handling errors
#...

# Local models
from tienda_lissa_app.models import ModelSales

# Local forms
from tienda_lissa_app import forms


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

class AddSales(TemplateView):

    """
    Create records and save in your model
    """
    # NOTE: To obtain request data, we depend from HTTP method:
    # GET METHOD: request.GET['any']   || request.GET.get('any')
    # POST METHOD: request.POST['any'] || request.POST.get('any')
    # POST METHOD: request.data['any'] || request.data.get('any')

    # Get form
    def get(self, request):

        try:

            template_name = "sales/sales_register.html"
            form = forms.FormSales()
            context = {"form":form}
            # Return form for create sale
            return render(request,template_name,context)

        except Exception as err:
            # Display template with error info
            return err

    # Post form
    def post(self,request):
        
        if request.POST == 'POST':
            try:
                # Counter variable from form atributes
                form =  forms.FormSales(request.POST)
                print("FORM POST",form)

                # validating
                form.validation_data()
                
                if form.is_valid():

                    total = 0

                    # Create new sale with values form
                    for sale in form:
                        last_record = sale['name']

                        # If the sale is from the same person
                        if last_record == sale['name']:
                            # Sum all prices from same person
                            total = total + sale['price']
                            newSale = ModelSales(
                                                sale['name'],
                                                sale['description'],
                                                sale['count'],
                                                sale['price'],
                                                sale['paid_out'],
                                                total)
                            newSale.save()
            except Exception as err:
                return err

        else:
            form = forms.FormSales()

#************|
# Read Sales:|
#************|

class ReadSales(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        
        data = ModelSales.objects.all()
        context = {"data":data}
        return super().get_context_data()


#**************|
# Search sales:|
#**************|
