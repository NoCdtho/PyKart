from django.urls import path
from . import views

#
# /products/1/detail

urlpatterns = [
    path('', views.index),
]
