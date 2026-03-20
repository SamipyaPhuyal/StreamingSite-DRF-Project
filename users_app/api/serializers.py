from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def save(self):
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password!=password2:
            raise serializers.ValidationError("error: p1 & p2 does not match")
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError("error: email already in use")
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError("error: user already exists")
        account=User.objects.create(username=self.validated_data['username'], email=self.validated_data['email'])
        account.set_password(password)
        account.save()
        return account