from django.db import models
from django.conf import settings
# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    product_type = models.CharField(max_length=264, blank=True, null= True)
    brand = models.CharField(max_length=264, blank=True, null= True)
    description = models.TextField(blank=True, null= True)
    budget_code = models.CharField(max_length=264, blank=True, null= True)
    date_of_purchase = models.DateField(blank=True, null= True)
    unit_price = models.FloatField()
    total_purchased = models.IntegerField()
    in_stock = models.IntegerField()
    total_price = models.FloatField(blank=True, null= True)    
    warrenty = models.FloatField(blank=True, null= True)
    financial_year = models.CharField(max_length=264, blank=True, null= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]



class Request(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    requested_for = models.CharField(max_length=256, blank=True, null=True)
    amount = models.IntegerField()
    Request_Created = models.DateField(auto_now_add=True)

    accepted = models.BooleanField(default=False)
    accepted_by = models.CharField(max_length=256, blank=True, null=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"{self.item} , requestd for {self.requested_for}, amount {self.amount}")

    class Meta:
        ordering = ['-Request_Created',]


