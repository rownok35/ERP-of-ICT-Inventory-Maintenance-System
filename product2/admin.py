from django.contrib import admin
from product2.models import Product_info, Item2, Request2

# Register your models here.

class Item_Admin2(admin.ModelAdmin):
    
    search_fields = ('model_name', 'product', 'brand', 'additional_info', 'item_code', 'invoice_number', 'voucher_number', 'seller_info', 'budget_code', 'budget_title', 'financial_year')
    list_filter = ('product', 'brand', 'seller_info', 'budget_title', 'financial_year')
    list_display = ('model_name', 'product', 'brand', 'unit_price', 'total_purchased', 'in_stock', 'warrenty')

admin.site.register(Product_info)
admin.site.register(Item2, Item_Admin2)
admin.site.register(Request2)