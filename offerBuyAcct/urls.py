# coding=utf-8

from django.urls import path

from . import views

urlpatterns = [
    path('', views.wei_xin),
    path('test/',views.test)
]
