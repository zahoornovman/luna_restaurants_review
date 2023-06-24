from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class DjangoUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)

    def __str__(self):
        return f'ID: {self.id} Email: {self.email}'

