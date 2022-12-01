from django.contrib import admin
from .models import EmployeeModel

# Register your models here.

@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'salary']
