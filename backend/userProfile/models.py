from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


DjangoUser = get_user_model()
# Create your models here.

class UserProfile(models.Model):
    django_user = models.OneToOneField(to=DjangoUser, on_delete=models.CASCADE, related_name='user_profile')
    description = models.TextField(max_length=1000, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


