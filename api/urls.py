
from django.urls import include, path

from api.views import auth as auth_views


router_config = {
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
}

auth_urls = [
    path('request_token/',
         auth_views.CustomkAuthToken.as_view(),
         name='request_token'),
    path('register/',
         auth_views.CustomkAuthToken.as_view(),
         name='register_request'),
]

urlpatterns = [
    path('auth/', include(auth_urls)),
]
