from django.contrib import admin
from app.users.models import User
from app.users.models import Contact


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
