from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.Item_all, name = "items"),
    path('add/', views.add_item, name = "add_items"),
    path('update/<str:id>/', views.update_item, name = "update_item"),
    path('details/<str:id>/', views.details, name = 'details'),

]
