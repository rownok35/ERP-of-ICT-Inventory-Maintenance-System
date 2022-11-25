from django.contrib import admin
from product.models import Item, Request
# Register your models here.

# class RequestAdmin(admin.ModelAdmin):
#     search_fields = ('name', 'product_type', 'brand', 'description')
#     list_filter = ('product_type', 'brand')
#     list_display = ('name', 'product_type', 'brand')


class Item_Admin(admin.ModelAdmin):
    
    search_fields = ('name', 'product_type', 'brand', 'description')
    list_filter = ('product_type', 'brand')
    list_display = ('name', 'product_type', 'brand')

admin.site.register(Item, Item_Admin)
admin.site.register(Request)