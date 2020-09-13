
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from app.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'
    objects = UserManager()

    username = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.id, self.username)

    @property
    def is_staff(self):
        return self.is_admin
