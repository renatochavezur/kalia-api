
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from app.users.managers import UserManager
from app.utils.users import generate_identification_code


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    objects = UserManager()

    username = models.CharField(max_length=128, unique=True)
    fullname = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=16, null=True, blank=True)
    email = models.CharField(max_length=128, null=True)
    is_admin = models.BooleanField(default=False)
    birth_day = models.DateField(null=True, blank=True)
    occupation = models.CharField(null=True, blank=True, max_length=64)
    dni = models.CharField(null=True, blank=True, max_length=32)

    show_occupation = models.BooleanField(default=True)
    show_phone = models.BooleanField(default=True)
    show_email = models.BooleanField(default=True)
    show_dni = models.BooleanField(default=True)
    show_birth_day = models.BooleanField(default=True)
    identification_code = models.CharField(max_length=16, unique=True, default=generate_identification_code)

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
