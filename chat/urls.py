# @Project:     HardwareHive
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        23-02-2023 02:25 pm
from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:item_pk>/', views.new_chat, name='new'),
]