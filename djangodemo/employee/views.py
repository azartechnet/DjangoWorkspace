from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse

from employee.models import Employee


def home(request):
    #return HttpResponse("This is the home Page")
    return render(request, 'employee/index.html')
def product(request):
    return HttpResponse("This is the product Page")
def simple_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        if username=="admin" and password=="admin":
           return redirect("home")
        else:
            #return HttpResponse("Invalid username or password")
            return render(request, 'employee/login.html', {'message': 'Invalid username or password'})
    return render(request, 'employee/login.html')

def register_form(request):
    return render(request, 'employee/register.html')

def employee_list(request):
    employees=Employee.objects.all()
    return render(request, 'employee/employee_list.html',{"employees":employees})

