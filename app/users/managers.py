
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, first_name='', last_name=''):
        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(username=self.model.normalize_username(username))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password=password)
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user
