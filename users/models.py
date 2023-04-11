from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True)
    is_employee = models.BooleanField(default=False)


class Employee(models.Model):
    is_superuser = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
