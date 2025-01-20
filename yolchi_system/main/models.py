from django.db import models
from django.contrib.auth.models import User 

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    APP_CHOICES = [
        ('YOL', 'راننده'),
        ('YUK', 'صاحب بار'),
    ]
    app = models.CharField(max_length=3, choices=APP_CHOICES)

    def __str__(self):
        return self.user.username + ":"+ self.app

# Create your models here.
