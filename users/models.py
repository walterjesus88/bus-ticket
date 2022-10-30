from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email= models.EmailField('email address',unique=True, 
        error_messages={
            'unique': 'A user with that email already exists.'
        })
    photo= models.ImageField(null=True,upload_to='users')
    dni = models.CharField(unique=True,null=True, max_length=255)
    city = models.CharField(null=True, max_length=255)
    country = models.CharField(null=True, max_length=255)
    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )
    def __str__(self):
        """Return username."""
        return self.username