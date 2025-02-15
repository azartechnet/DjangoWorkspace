from turtle import home
from django.urls import path

from . import views

from . views import home, simple_login

urlpatterns=[
path('',home,name='home'),
path('product/',views.product),
path('login/',simple_login,name="login")
]