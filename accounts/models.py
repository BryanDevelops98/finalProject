from django.contrib.auth.models import AbstractUser
from django.db import models
from taxiApp import models

# Create your models here.

# Add property is_driver to indicate if the user is a driver
# Add foreign key to Car table (User can have car associated if they are a Driver `is_driver` == True)
# Add property phonenumber (Charfield [no validation for now] could use python package?)

# class User(AbstractUser):
#     pass