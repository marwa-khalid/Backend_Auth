from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BrandManager(models.Model):
    class Meta:
        app_label = 'backend'
        
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='brand_manager_pictures')

    def __str__(self):
        return self.email

class PRManagerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        class Meta:
            app_label = 'backend'
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class PRManager(AbstractBaseUser):
    class Meta:
        app_label = 'backend'
    email = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = PRManagerManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.is_staff
