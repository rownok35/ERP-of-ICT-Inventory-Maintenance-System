from django.shortcuts import render
from product2.models import Item2, Request2, Product_info
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product2.forms import ProductInfoForm, ItemForm2
from django.shortcuts import HttpResponseRedirect 
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
import datetime


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch





@login_required
def item_category(request):
    form = ProductInfoForm()
    if request.method == 'POST':
        form = ProductInfoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('product:items'))
    return render(request, 'product2/add_category.html', context={'form': form})