from django.contrib.auth import get_user_model
from django.db import models

import userProfile

# Create your models here.


class Review(models.Model):
    content = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=userProfile, on_delete=models.CASCADE, related_name='review_written')
    liked_by = models.ForeignKey(to=userProfile, on_delete=models.CASCADE, related_name='review_liked')
    # restaurant
