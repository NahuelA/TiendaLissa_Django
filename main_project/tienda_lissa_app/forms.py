from email.mime import base
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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

    # Validations for inputs
    def validation_data(self):

        # Validate all fields
        valid_int = self.cleaned_data['count']
        valid_decimal = self.cleaned_data['price']

        try:

            # VALIDATE INTEGERS
            if str(valid_int).isdigit():
                print("Adding valid field(INT)",valid_int)
            else:
                raise ValidationError(
                _('Invalid string: %(value)s'),
                code='invalid',
                params={'value': valid_int},
            )

            # VALIDATE DECIMALS
            if str(valid_decimal).isdigit():
                print("Adding valid field(DECIMAL)", valid_decimal)
            else:
                raise ValidationError(
                _('Invalid string: %(value)s'),
                code='invalid',
                params={'value': valid_decimal},
            )

        except:
            raise ValidationError(
            _('Invalid input: %(value)s'),
            code='invalid',
            params={'value': 'Not expecting'},
        )

