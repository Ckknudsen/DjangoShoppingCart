from django.db import models
# Create your models here.


class Item(models.Model):
    itemId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Event(Item):
    date = models.DateTimeField(max_length=20)


