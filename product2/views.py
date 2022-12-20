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

@login_required
def item_add(request):
    form = ItemForm2()
    if request.method == 'POST':
        form = ItemForm2(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.in_stock = form.total_purchased
            form.save()
            return HttpResponseRedirect(reverse('product:items'))
    return render(request, 'product2/add_item.html', context={'form': form})


@login_required
def Item_all(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    
    if search_query == '':
        items = Item2.objects.all()
    else:
        items = Item2.objects.filter(Q(model_name__icontains = search_query) | Q(brand__icontains = search_query) | Q(item_code__icontains = search_query) | Q(invoice_number__icontains = search_query) | Q(voucher_number__icontains = search_query) | Q(seller_info__icontains = search_query) | Q(budget_code__icontains = search_query) | Q(budget_title__icontains = search_query) | Q(financial_year__icontains = search_query))

    #Pagination
    showing_product = 20
    paginator = Paginator(items, showing_product)
    page = request.GET.get('page')

    try:
        page_product = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_product = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_product = paginator.page(page)
    
    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 10)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    total_items = len(items)
    showing_items = len(page_product)


    return render(request,  'product2/Items.html', {'items': page_product, 'total_items':total_items, 'showing_items': showing_items, 'custom_range': custom_range,})


@login_required
def details(request, id):    

    item = Item2.objects.get(id = id)
    # granted_items = Request.objects.filter(Q(item__id = item.id) & Q(accepted = True))
    # print('granted_items', granted_items)
    context = {'item': item, }
    return render(request, 'product2/details.html', context)
