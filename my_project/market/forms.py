from django.forms import ModelForm
# from django.forms.fields import 
from . models import Product


class ProductForm(ModelForm):
    # TODO: add submit button
    class Meta:
        model = Product
        exclude = []
