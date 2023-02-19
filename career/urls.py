# @Project:     HardwareHive
# @Filename:    urls.py
# @Author:      Daksh
# @Time:        19-02-2023 12:20 pm

from django.urls import path
from . import views

app_name = 'career'

urlpatterns = [
    path('', views.index, name='careers'),
    ]
