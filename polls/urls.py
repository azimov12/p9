from django.shortcuts import render
from .views import index, index2, index3
from django.urls import path

urlpatterns = [
    path('index1/', index),
    path('index2/', index2),
    path('index3/', index3)
]