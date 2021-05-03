from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import phone_validator


class User(AbstractUser):
    username = models.CharField(max_length=11, validators=[phone_validator], unique=True)
