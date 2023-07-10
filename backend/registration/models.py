from django.contrib.auth import get_user_model
from django.db import models
import random

# Create your models here.


DjangoUser = get_user_model()


def random_code_generator(length=6):
    code = "".join(random.choice('0123456789') for _ in range(length))
    return code


class Registration(models.Model):
    email = models.EmailField(unique=True, blank=False)
    code = models.IntegerField(default=random_code_generator)
    django_user = models.OneToOneField(to=DjangoUser, on_delete=models.CASCADE, related_name="registration")
