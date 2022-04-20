from django.forms import ModelForm
from tienda_lissa_app.models import ModelSales
# Form for create sales
class FormSales(ModelForm):
    class Meta:
        model = ModelSales
        fields = ['name','description','count','price','paid_out']

