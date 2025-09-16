from django.db import models


# Create your models here.
class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    brnd = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    year = models.DateField()

