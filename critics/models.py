from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Critic(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    create_at=models.DateField(auto_now_add=True)
    creator=models.models.Foreign_key(User,on_delete=models.CASCADE)
    