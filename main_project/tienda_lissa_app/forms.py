from django import forms

# Form for create sales
class FormSales(forms.Form):

    # Atributes for form
    # NOTE: date_creation and total fields, it will be created dynamically
    name = forms.CharField(label="Nombre",
                           max_length=50,
                           required=True,
                           help_text="Ingrese su nombre")

    description = forms.CharField(label="Descripción",
                                  max_length=120,
                                  help_text="Ingrese una descripción de su producto",
                                  widget=forms.Textarea())

    count = forms.IntegerField(label="Cantidad",min_value=0,required=True)
    price = forms.DecimalField(label="Precio",min_value=0,required=True)
    # Defaul value is True
    paid_out = forms.BooleanField(label="Pagado",
                                  initial=True,
                                  help_text="Si es verdadero, está pagado",
                                  widget=forms.CheckboxInput())