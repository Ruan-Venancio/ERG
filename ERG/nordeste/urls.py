from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='nordeste'),
    path('/pernanmbuco', views.pe, name='pe'),
    path('/rio-grande-do-norte', views.rn, name='rn')
]