from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class User(AbstractUser):
    phone_no=models.CharField(max_length=12,unique=True)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6)

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS=[]
    objects=UserManager()