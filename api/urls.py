
from django.urls import include, path

from api.views import auth as auth_views
from api.views import users as user_views
from api.views import events as event_views

auth_urls = [
    path('request_token/',
         auth_views.CustomkAuthToken.as_view(),
         name='request_token'),
    path('register/',
         auth_views.RegisterView.as_view(),
         name='register_request'),
]

event_urls = [
    path('<int:id>/',
         event_views.EventView.as_view(),
         name='event_description'),
]

user_urls = [
    path('',
         user_views.UserDataView.as_view(),
         name='update_user_data'),
]

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('users/', include(user_urls)),
    path('events/', include(event_urls)),
]
