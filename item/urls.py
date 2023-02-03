# @Project:     HardwareHive
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        04-02-2023 12:50 am

from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.item_detail, name='item-detail'),
    ]