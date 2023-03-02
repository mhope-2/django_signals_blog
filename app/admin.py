from django.contrib import admin
from .models import Employee, EmployeeProfile

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeProfile)