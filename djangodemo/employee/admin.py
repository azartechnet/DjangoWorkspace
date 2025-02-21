from django.contrib import admin

from employee.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'email', 'phone_number','address','role')

    
