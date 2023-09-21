from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.full_name


class Address(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=25)
    address = models.TextField()
    postal_code = models.IntegerField()
    phone_number = models.CharField(max_length=11)

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"

    def __str__(self):
        return f"{self.city} - {self.address}"
