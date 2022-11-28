from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.Item_all, name = "items"),
    path('add/', views.add_item, name = "add_items"),
    path('update/<str:id>/', views.update_item, name = "update_item"),
    path('details/<str:id>/', views.details, name = 'details'),
    path('request/<str:id>/', views.request_item, name = 'request_item'),
    path('requests', views.all_request, name = 'all_request'),
    path('accept/<str:id>/', views.accepted_item, name = 'accepted_item'),
    path('reject/<str:id>/', views.rejected_item, name = 'rejected_item'),

]
