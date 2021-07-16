from users.models import Profile , Follower

from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers




class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class FollwerSerializer(ModelSerializer):
    following = UserSerializer(many=True ,read_only=True)
    user =UserSerializer()
    class Meta:
        model = Follower
        fields = ['following' ,'user' ]



class ProfileSerializer(ModelSerializer):
    user  = UserSerializer()
    class Meta:
        model = Profile
        fields = ["user" , "picture", "bio" , "location"]


