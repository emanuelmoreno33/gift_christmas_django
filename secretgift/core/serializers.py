from rest_framework import serializers
from .models import UserSend,UserProfile

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(required=False)
    name = serializers.CharField(max_length=200,required=False)
    image = serializers.ImageField(required=False)
    email = serializers.EmailField(required=False)
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'image', 'email']