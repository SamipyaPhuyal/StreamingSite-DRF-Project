from django.shortcuts import render
from users_app.api.serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
#from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

class RegistrationAPIView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            # refresh=RefreshToken.for_user(account)
            token=Token.objects.create(user=account)
            data={
                "response":"successfully registered a new user",
                "username":account.username,
                "email":account.email,
                # 'refresh': str(refresh),
                # 'access': str(refresh.access_token),
                "token":str(token)
            }
        else:
            data=serializer.errors
        return Response(data)   
        
class LogoutAPIView(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'success': 'You have been logged out'})