from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from users_app.views import LogoutAPIView, RegistrationAPIView 

urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    path('register/',RegistrationAPIView.as_view(),name="register"),
    path('logout/',LogoutAPIView.as_view(),name="logout"),
]
