from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    """Custom user model"""
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=20)
    is_employee = models.BooleanField(default=False)
    is_restaurant = models.BooleanField(default=False)
    objects = CustomUserManager
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Employee(models.Model):
    """Employee model"""
    employee = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Restaurant(models.Model):
    """Restaurant model"""
    restaurant = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
