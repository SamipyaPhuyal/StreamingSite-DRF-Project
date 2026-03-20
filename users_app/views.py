from django.shortcuts import render
from users_app.api.serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class RegistrationAPIView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
class LogoutAPIView(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response({'success': 'You have been logged out'})