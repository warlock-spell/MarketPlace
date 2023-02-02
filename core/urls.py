# @Project:     HardwareHive
# @Filename:    urls.py.py
# @Author:      Daksh
# @Time:        02-02-2023 07:46 pm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms/', views.terms, name='terms'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    ]