from django.forms import ModelForm

from mainApp.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]