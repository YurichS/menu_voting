from django.db import models
from accounts.models import Restaurant


# Create your models here.

class Menu(models.Model):
    menu = models.CharField(max_length=1000)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
