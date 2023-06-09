from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.

class Seat(models.Model):
    seat_number  = models.IntegerField(unique=True)
    is_booked = models.BooleanField(default=False)
    myuser = models.CharField(max_length=350)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.seat_number)
    

    
