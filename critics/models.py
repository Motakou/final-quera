from django.db import models
from django.contrib.auth.models import User

class Critic(models.Model):
    title = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255, )
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    creator_first_name = models.CharField(max_length=255)
    creator_last_name = models.CharField(max_length=255)


    def __str__(self):
        return self.title
