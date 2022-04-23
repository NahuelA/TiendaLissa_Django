# Form and widgets
from django.forms import (
    ModelForm,
    Textarea,
    DecimalField,
    NumberInput
)
# Model
from tienda_lissa_app.models import ModelSales

# Form for create sales
class FormSales(ModelForm):
    
    class Meta:
        model = ModelSales
        fields = ['name','description','count','price','paid_out']

        # Custom widgets and fields
        labels = {

            'name':'Nombre',
            'description':'Descripción',
            'count':'Cantidad',
            'price':'Precio',
            'paid_out':'Pagado',
        }
        widgets = {

            'description':Textarea(attrs={'cols':80,'rows':20}),
            'price': NumberInput(attrs={'widget':DecimalField(
                                                            min_value=0,
                                                            max_digits=10,
                                                            decimal_places=2,
                                                            required=True),'min':0})
        }

