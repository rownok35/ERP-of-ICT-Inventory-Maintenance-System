from django.forms import ModelForm
from product2.models import Item2, Request2, Product_info
from django import forms


class ProductInfoForm(ModelForm):
    class Meta:
        model = Product_info
        exclude = ('user', 'created', 'updated')


class ItemForm2(ModelForm):
    class Meta:
        model = Item2
        exclude = ('user', 'created', 'updated', 'in_stock')
        widgets = {
        'date_of_purchase': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}