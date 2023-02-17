from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Category(models.Model):
    """Category class model"""
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class User(AbstractUser):
    """User class model"""
    email = models.EmailField(unique=True)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Employee(models.Model):
    """Employee class model"""

    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Restaurant(models.Model):
    """Restaurant class model"""
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Menu(models.Model):
    """Menu class model"""
    restaurant = models.ForeignKey(
        Restaurant,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    menu = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.restaurant.name


class Vote(models.Model):
    """Vote class model"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.employee}'
