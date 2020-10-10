
from django.urls import include, path
from rest_framework import routers

from api.views.events import EventViewSet
from api.views.auth import AuthAPIViewSet
from api.views.users import UserViewSet

router = routers.DefaultRouter()
router.register('auth', AuthAPIViewSet, basename='auth_token')
router.register('events', EventViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
