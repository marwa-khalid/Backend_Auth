from django.contrib.auth.models import AbstractUser
from django.db import models

class BrandManager(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/')
    # other fields for the brand manager

    def __str__(self):
        return self.email
