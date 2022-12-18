from django.urls import path
from . import views

app_name = "product2"

urlpatterns = [
    path('item-category/', views.item_category, name = 'item_category')

]