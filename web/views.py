from django.shortcuts import render

from rest_framework import generics  
from .serializers import (PostSerializer,CategorySerializer 
, savepostSerializer ) 
from .models import Post ,Category ,SavePost 
from rest_framework.viewsets import  ViewSet


# class PostViewSet(ViewSet):
#     queryset=Profile.objects.all()
#     serializer_class = ProfileSerializer


# class CatgoryViewSet(ViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer



class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(status='P')
    serializer_class = PostSerializer

class PosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.filter(status='P')
    serializer_class = PostSerializer

class CatgoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class savedPostList(generics.ListCreateAPIView):
    queryset = SavePost.objects.all()
    serializer_class = savepostSerializer

