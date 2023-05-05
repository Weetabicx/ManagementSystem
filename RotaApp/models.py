from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    departments = [
        ("Reception", "Reception Staff"),
        ("Function", "Function Staff"),
        ("Restaurant", "Restaurant Staff")
    ]

    employeeID = models.AutoField(unique=True, primary_key=True)
    management = models.BooleanField(default=False)
    department = models.CharField(max_length=16, choices=departments)
    availability = models.CharField(max_length=16)