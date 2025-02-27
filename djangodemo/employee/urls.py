from turtle import home
from django.urls import path

from . import views

from . views import home, simple_login,register_form,employee_list

urlpatterns=[
path('',home,name='home'),
path('product/',views.product),
path('login/',simple_login,name="login"),
path('register/',register_form,name="register"),
path('employees/',employee_list,name="employee_list")
]