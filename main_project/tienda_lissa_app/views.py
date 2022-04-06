# For render templates context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader

# For handling errors
from django.shortcuts import get_object_or_404
from django.http import Http404

# Models
from tienda_lissa_app.models import TiendaLissa

#=======================
# Views for class
#=======================

# The master class-based base view. All other
# class-based views inherit from this base class
from django.views.generic.base import (

    # TemplateView and RedirectView inherit View class
    TemplateView, RedirectView
)

# Libraries of thirds
import datetime

#=======================
# Create your views here.
#=======================

# Tests
def tests(request):
    # Views with functions
    # Example
    date_now = datetime.datetime.now()
    content = "<html><body>It is now %s.</body></html>" % date_now
    
    # Englobe in try/except
    try:
        print(HttpResponse(status=201,content=content).getvalue())
        return HttpResponse(status=201,content=content)
    except Exception:
        return Http404()


# Views in class
# Example:
# class MyView(View):
    # Flowchart:
        # setup()
        # dispatch()
        # http_method_not_allowed()
        # options()

    # Attributes for View class
    # http_method_names = List ['get', 'post', 'put',
    #                           'patch', 'delete', 'head',
    #                           'options', 'trace']

    # def get(self, request, *args, **kwargs):
    #     method_name = self.http_method_names[0] # This get method
    #     return HttpResponse(f'Hello, World!{method_name}') # Response get

class Templates(TemplateView):
    # Flowchart:
        # setup()
        # dispatch()
        # http_method_not_allowed()
        # get_context_data()

    # Template name
    template_name = "test.html"
    # Context for template
    # You can also add context using the extra_context keyword argument for as_view().
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = TiendaLissa.objects.all()[:5]
        return context

class Redirecting(RedirectView):
    # Flowchart:
        #setup()
        # dispatch()
        # http_method_not_allowed()
        # get_redirect_url()
    
    permanent = False
    query_string = True
    pattern_name = 'my-view'

    def get_redirect_url(self, *args, **kwargs):
        # article = get_object_or_404(TiendaLissa, pk=kwargs['pk'])
        # article.update_counter()
        return super().get_redirect_url(*args, **kwargs)

# My crud
class CrudSales(TemplateView):
    # Vars
    # template_name = ""
        # Attributes for View class
    # http_method_names = List ['get', 'post', 'put',
    #                           'patch', 'delete', 'head',
    #                           'options', 'trace']

    if TemplateView.http_method_names.index == 1:

        try:
            a = TiendaLissa(name=name,
                            description=description,
                            count=count,
                            price=price,
                            paid_out=paid_out)
            # a.save()
            # a.delete()
        except:
            pass
class Index(TemplateView):

    
    def index(request):
        latest_question_list = TiendaLissa.objects.order_by('-pub_date')[:5]
        template = loader.get_template('polls/index.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))