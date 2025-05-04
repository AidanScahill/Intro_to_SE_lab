from django import forms
from inventory.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'num_in_stock', 'category', 'image_url']
        