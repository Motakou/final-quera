from django.db import models
from django.contrib.auth.models import User

class user(User):
    #first_name = models.Charfield(max_length=255)
    #Last_name = models.Charfield(max_length=255)
    pass

class Critic(models.Model):
    title = models.CharField(max_length=255)
    #movie_title = models.Charfield(max_length=255)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    """rating = (
        (5, 'Great'),
        (4, 'Good'),
        (3, 'Normal'),
        (2, 'Weak'),
        (1, 'So Bad'),
    )
    rate = models.i(choices = rating)"""
