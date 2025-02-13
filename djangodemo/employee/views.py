from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    #return HttpResponse("This is the employee Page")
    return render(request, 'home.html')
def product(request):
    return HttpResponse("This is the product Page")

