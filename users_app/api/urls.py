from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from users_app.views import LogoutAPIView, RegistrationAPIView 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('register/',RegistrationAPIView.as_view(),name="register"),
    path('logout/',LogoutAPIView.as_view(),name="logout"),
]
