# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM:

### models.py
```
from django.db import models


# Create your models here.
class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    brnd = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.DateField()


```

### admin.py:

```
from django.contrib import admin
from . models import Car
# Register your models here.
admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('emp_id','name','desig','salary','doj')

```



## OUTPUT

Include the screenshot of your admin page.


![alt text](<../Screenshot 2025-09-16 102833.png>)

![alt text](<../Screenshot 2025-09-16 103051.png>)




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
