from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    date_of_birth = models.DateField()
