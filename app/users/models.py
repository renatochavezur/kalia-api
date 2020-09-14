
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from app.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    objects = UserManager()

    username = models.CharField(max_length=128, unique=True)
    fullname = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=128, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin
