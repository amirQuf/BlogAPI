from django.shortcuts import render
from rest_framework import generics
from .serialzers import ProfileSerializer , UserSerializer , FollwerSerializer
from .models import Profile ,Follower
from django.contrib.auth.models import User


class Profileview(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class = ProfileSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowerList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollwerSerializer