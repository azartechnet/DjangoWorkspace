from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    #return HttpResponse("This is the home Page")
    return render(request, 'employee/index.html')
def product(request):
    return HttpResponse("This is the product Page")

