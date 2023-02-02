# @Project:     HardwareHive
# @Filename:    urls.py.py
# @Author:      Daksh
# @Time:        02-02-2023 07:46 pm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    ]