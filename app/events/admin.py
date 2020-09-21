from django.contrib import admin

from app.events.models import Event
from app.events.models import Enrollment


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    pass
