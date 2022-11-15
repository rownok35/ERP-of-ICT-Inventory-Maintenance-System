from django.db import models
from django.conf import settings
# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    product_type = models.CharField(max_length=264, blank=True, null= True)
    brand = models.CharField(max_length=264, blank=True, null= True)
    description = models.TextField(blank=True, null= True)
    date_of_purchase = models.DateField()
    unit_price = models.FloatField()
    total_purchased = models.IntegerField()
    in_stock = models.IntegerField()
    total_price = models.FloatField(blank=True, null= True)    
    warrenty = models.FloatField(blank=True, null= True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created',]