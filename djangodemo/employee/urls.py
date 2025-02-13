from turtle import home
from django.urls import path

from . import views

urlpatterns=[
path('',home,name='home'),
path('product/',views.product),
]