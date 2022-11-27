from django.forms import ModelForm
from product.models import Item, Request
from django import forms

class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('user', 'created', 'updated')
        widgets = {
        'date_of_purchase': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}

class RequestForm(ModelForm):
    class Meta:
        model = Request
        exclude = ('item', 'requested_by', 'request_created', 'accepted', 'accepted_by', 'accepted_at', 'rejected', 'remarks','rejected_by', 'rejected_at')