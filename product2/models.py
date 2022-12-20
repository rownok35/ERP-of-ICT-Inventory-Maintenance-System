from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

# Create your models here.

class Product_info(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product_Category = models.CharField(max_length=512)
    description = models.TextField(blank=True, null= True)

    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_Category

    class Meta:
        ordering = ['-created',]
    

class Item2(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product_info,on_delete=models.CASCADE)
    model_name = models.CharField(max_length=500, blank=True, null= True)
    brand = models.CharField(max_length=264, blank=True, null= True)
    additional_info = models.TextField(blank=True, null= True)
    
    item_code = models.CharField(max_length=264, blank=True, null= True)
    invoice_number = models.CharField(max_length=264, blank=True, null= True)
    voucher_number = models.CharField(max_length=264, blank=True, null= True)
    

    seller_info = models.TextField(blank=True, null= True)
    
    date_of_purchase = models.DateField(blank=True, null= True)
    unit_price = models.FloatField()
    total_purchased = models.IntegerField()
    in_stock = models.IntegerField()
    # total price will be calculated using multiplied by unit_price*total_purchased   
    warrenty = models.FloatField(blank=True, null= True)
    budget_code = models.CharField(max_length=264, blank=True, null= True)
    budget_title = models.CharField(max_length=264, blank=True, null= True)
    financial_year = models.CharField(max_length=264, blank=True, null= True)
    created = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(auto_now=True)


    def total_price(self):
        return self.unit_price*self.total_purchased



    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ['-created',]
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

dept_wing = (
    ('Other', 'Other'),
    ('CE','CE'),
    ('ARCH','ARCH'),
    ('PME','PME'),
    ('CSE','CSE'),
    ('EECE','EECE'),
    ('CE','CE'),
    ('ME', 'ME'),
    ('AE','AE'),
    ('NAME','NAME'),
    ('IPE','IPE'),
    ('NSE','NSE'),
    ('BME','BME'),
    ('SH','SH'),
    ('Office of The Commandant','Office of The Commandant'),
    ('MIST Secretariat','MIST Secretariat'),
    ('Academic Wing','Academic Wing'),
    ('Administration Wing','Administration Wing'),
    ('Research & Development Wing','Research & Development Wing'),
    ('Directorate of Student Welfare','Directorate of Student Welfare'),
    ('Directorate of Information and Communication Technology','Directorate of Information and Communication Technology'),
    ('Office of the Controller of Examination','Office of the Controller of Examination'),

)

class Request2(models.Model):


    item = models.ForeignKey(Item2, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    requested_for = models.CharField(max_length=256, choices=dept_wing)
    additional_info = models.CharField(max_length=256, blank=True, null= True)

    quantity = models.IntegerField()
    request_created = models.DateTimeField(default=datetime.datetime.now)

    remarks = models.CharField(max_length=1000, blank=True, null=True)

    accepted = models.BooleanField(default=False)
    accepted_by = models.CharField(max_length=256, blank=True, null=True)
    accepted_at = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)


    rejected = models.BooleanField(default=False)
    rejected_by = models.CharField(max_length=256, blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)

    

 

    def __str__(self):
        return (f"{self.item} , requestd for {self.requested_for}, amount {self.amount}")

    class Meta:
        ordering = ['-request_created',]
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'


