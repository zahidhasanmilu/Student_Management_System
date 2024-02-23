from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    USER_TYPE = (
        ('1', 'HOD'),
        ('2', 'STAFF'),
        ('3', 'STUDENT'),
    )

    user_type = models.CharField(choices=USER_TYPE, max_length=50, default=1)
    email = models.EmailField(unique=True,)
    profile_pic = models.ImageField(
        upload_to='Profile_Pics/', default='demo_profilepic.jpg')
