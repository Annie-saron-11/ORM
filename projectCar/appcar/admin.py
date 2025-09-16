from django.contrib import admin
from . models import Car
# Register your models here.
admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('emp_id','name','desig','salary','doj')
