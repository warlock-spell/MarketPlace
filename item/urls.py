# @Project:     HardwareHive
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        04-02-2023 12:50 am

from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.item_detail, name='item-detail'),
    path('<int:pk>/delete/', views.delete_item, name='delete-item'),
    path('<int:pk>/edit/', views.edit_item, name='edit-item'),
    path('new/', views.new_item, name='new-item'),
    path('', views.browse_items, name='browse-item'),
    path('buy-item/<int:pk>/', views.buy_item, name='buy-item'),
    path('order-confirmed/<int:pk>/', views.order_confirmed, name='order-confirmed'),
]