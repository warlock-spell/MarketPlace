# @Project:     HardwareHive
# @Filename:    urls.py.py
# @Author:      Daksh
# @Time:        02-02-2023 07:46 pm

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('terms/', views.terms, name='terms'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='core/login.html'),
         name='login'),
]
