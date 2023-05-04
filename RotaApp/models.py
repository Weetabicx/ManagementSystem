from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    companies = [
        ("Glynhill", "Glynhill Hotel LTD")
    ]
    departments = [
        ("Reception", "Reception Staff"),
        ("Function", "Function Staff"),
        ("Restaurant", "Restaurant Staff")
    ]

    employeeID = models.AutoField(unique=True, primary_key=True)
    company = models.CharField(max_length=16, choices=companies)
    management = models.BooleanField()
    department = models.CharField(max_length=16, choices=departments)
    availability = models.CharField(max_length=16)