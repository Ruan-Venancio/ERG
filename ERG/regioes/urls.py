from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='regioes'),
    path('sul', include('sul.urls')),
    path('nordeste', include('nordeste.urls')),
]
