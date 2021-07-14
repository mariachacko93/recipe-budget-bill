from django import forms
from django.forms import ModelForm
from billing.models import Products,Purchase
class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["product_name"]
class AddPurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ["product","qty","purchase_price","selling_price"]