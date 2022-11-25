from django.shortcuts import render
from product.models import Item, Request
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.forms import ItemForm, RequestForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
# Create your views here.

@login_required
def Item_all(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # print("search_query: ",search_query)
    # items = Item.objects.filter()
    
    if search_query == '':
        items = Item.objects.filter()
    else:
        items = Item.objects.filter(Q(name__icontains = search_query) | Q(product_type__icontains = search_query) | Q(brand__icontains = search_query) | Q(budget_code__icontains = search_query))

    #Pagination
    showing_product = 50
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


    return render(request,  'product/Items.html', {'items': page_product, 'total_items':total_items, 'showing_items': showing_items, 'custom_range': custom_range,})

@login_required
def details(request, id):    

    item = Item.objects.get(id = id)
    context = {'item': item}
    return render(request, 'product/details.html', context)


@login_required
def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('product:items'))
    return render(request, 'product/add_item.html', context={'form': form})


@login_required
def request_item(request, id):
    item = Item.objects.get(pk=id)
    in_stock = item.in_stock
    form = RequestForm()

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            
            form = form.save(commit=False)

            if form.amount > in_stock:
                
                messages.warning(request, "Item Amount must be less than In Stock")
                return HttpResponseRedirect(reverse('product:request_item', args=(id,)))
            form.item = item
            form.requested_by = request.user
            form.save()
            messages.success(request, "Request Added!!")
            return HttpResponseRedirect(reverse('product:items'))
    
    return render(request, 'product/request_item.html', context={'form': form, 'item': item})



@login_required
def update_item(request, id):
    item = Item.objects.get(pk=id)
    date_of_purchase = item.date_of_purchase
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance= item)

        if form.is_valid():
            form = form.save(commit=False)
            if form.date_of_purchase == None:
                form.date_of_purchase = date_of_purchase                
            form.save()
            messages.success(request, "Change Saved!!")
            form = ItemForm(instance=item)
            return HttpResponseRedirect(reverse('product:update_item', args=(id,)))
    return render(request, 'product/add_item.html', context={'form':form})