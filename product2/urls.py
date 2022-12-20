from django.urls import path
from . import views

app_name = "product2"

urlpatterns = [
    path('item-category/', views.item_category, name = 'item_category'),
    path('item-add/', views.item_add, name = 'item_add'),
    path('', views.Item_all, name = 'Item_all'),
    path('details/<str:id>/', views.details, name = 'details'),

]