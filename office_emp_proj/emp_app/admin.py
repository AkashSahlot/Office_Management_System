from django.contrib import admin
from .models import Employee, Role, Department
# Register your models here.



'''
To register the Data of Employee, Role and their department we use this admin.site.register
'''
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)

