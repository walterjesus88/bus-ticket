from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
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
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number=models.CharField(validators=[phone_regex],max_length=17,blank=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified=models.BooleanField(
        'verified',default=True,help_text='Set to true when the user have verified its email address.'
    )


    def __str__(self):
        """Return username."""
        return self.username

class Profile(models.Model):
    """Profile model.
    A profile a user's public biography, picture,  and statistics. """
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """Return user's str representation."""
        return str(self.user)
