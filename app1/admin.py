from django.contrib import admin
from app1.models import Employee
class Employeeadmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']
admin.site.register(Employee,Employeeadmin)


