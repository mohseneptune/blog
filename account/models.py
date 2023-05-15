from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    GENDER_CHOICES = (('male', 'Male'),('female', 'Female'))

    gender = models.CharField(max_length=6, blank=False, choices=GENDER_CHOICES, default='Male')

    def __str__(self) -> str:
        return self.username
    

# python manage.py createsuperuser --email admin@example.com --username admin