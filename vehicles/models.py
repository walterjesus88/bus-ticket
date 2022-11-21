from django.db import models

from users.models import User
# Create your models here.
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    photo= models.ImageField(null=True,upload_to='users')
    license = models.CharField(unique=True,null=True, max_length=255)
    type = models.CharField(null=True, max_length=255)
    available_seats = models.PositiveSmallIntegerField(default=1)
    passengers = models.ManyToManyField('users.User', related_name='passengers', blank=True)

    def __str__(self):
        """Return username."""
        return self.name