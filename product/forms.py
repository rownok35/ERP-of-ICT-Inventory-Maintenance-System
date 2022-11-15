from django.forms import ModelForm
from product.models import Item
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('user', 'created', 'updated')
        widgets = {
        'date_of_purchase': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}