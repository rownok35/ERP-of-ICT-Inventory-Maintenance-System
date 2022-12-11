from django.shortcuts import render
from product.models import Item, Request
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from product.forms import ItemForm, RequestForm
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
def report_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    c = canvas.Canvas(buffer, pagesize = letter, bottomup = 0)

    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    lines = ["this is line1", "this is line2", "this is line3"]

    for line in lines:
        textobj.textLine(line)

    c.drawText(textobj)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

@login_required
def report_wing(request, name):
    reports = Request.objects.filter(Q(requested_for=name) & Q(accepted = True))
    # print("reports ",reports)
    return render(request, 'product/reports.html',{'reports':reports})




@login_required
def Item_all(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    # print("search_query: ",search_query)
    # items = Item.objects.filter()
    
    if search_query == '':
        items = Item.objects.all()
    else:
        items = Item.objects.filter(Q(name__icontains = search_query) | Q(product_type__icontains = search_query) | Q(brand__icontains = search_query) | Q(budget_code__icontains = search_query))

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


    return render(request,  'product/Items.html', {'items': page_product, 'total_items':total_items, 'showing_items': showing_items, 'custom_range': custom_range,})

@login_required
def details(request, id):    

    item = Item.objects.get(id = id)
    granted_items = Request.objects.filter(Q(item__id = item.id) & Q(accepted = True))
    print('granted_items', granted_items)
    context = {'item': item, 'granted_items':granted_items}
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
def all_request(request):
    requests = Request.objects.all()


    #Pagination
    showing_product = 20
    paginator = Paginator(requests, showing_product)
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


    total_items = len(requests)
    showing_items = len(page_product)

    return render(request, 'product/all_request.html', context={'requests': page_product, 'total_items':total_items, 'showing_items': showing_items, 'custom_range': custom_range,})

@login_required
def rejected_item(request, id):
    request_item = Request.objects.get(id=id)
    request_item.rejected = True
    a = str(request.user)

    request_item.rejected_by = a
    request_item.rejected_at = datetime.datetime.now()
    request_item.save()


    return HttpResponseRedirect(reverse('product:all_request'))

@login_required
def accepted_item(request, id):
    request_item = Request.objects.get(id=id)
    request_item.accepted = True
    a = str(request.user)

    request_item.accepted_by = a
    request_item.accepted_at = datetime.datetime.now()
    request_item.save()

    item = Item.objects.get(id = request_item.item.id)
    item.in_stock -= request_item.amount 
    item.save()


    return HttpResponseRedirect(reverse('product:details', args=(request_item.item.id,)))

@login_required
def grant_item(request, id):
    item = Item.objects.get(pk=id)
    in_stock = item.in_stock
    form = RequestForm()

    if request.user.is_superuser:

        if request.method == 'POST':
            form = RequestForm(request.POST)
            if form.is_valid():
                
                form = form.save(commit=False)

                if form.amount > in_stock:
                    
                    messages.warning(request, "Item Amount must be less than or equal In Stock")
                    return HttpResponseRedirect(reverse('product:grant_item', args=(id,)))
                form.item = item
                form.requested_by = request.user
                form.accepted = True
                a = str(request.user)
                form.accepted_by = a
                form.accepted_at = datetime.datetime.now()
                form.save()
                messages.success(request, "Item approved!!")
                return HttpResponseRedirect(reverse('product:details', args=(item.id,)))
        return render(request, 'product/request_item.html', context={'form': form, 'item': item})    
    else:
        messages.warning(request, "You are not allowed to view that page")
        return HttpResponseRedirect(reverse('product:items'))
    
    


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
                
                messages.warning(request, "Item Amount must be less than or equal In Stock")
                return HttpResponseRedirect(reverse('product:request_item', args=(id,)))
            form.item = item
            form.requested_by = request.user
            form.save()
            messages.success(request, "Request Added!!")
            return HttpResponseRedirect(reverse('product:all_request'))
    
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