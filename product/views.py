from django.shortcuts import render
from product.models import Item
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.forms import ItemForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.

@login_required
def Item_all(request):

    items = Item.objects.all()

    #Pagination
    showing_product = 5
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
def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance= item)
        if form.is_valid():
            form.save()
            messages.success(request, "Change Saved!!")
            form = ItemForm(instance=item)
            return HttpResponseRedirect(reverse('product:update_item', args=(id,)))
    return render(request, 'product/add_item.html', context={'form':form})