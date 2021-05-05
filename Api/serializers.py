from web.models import Post ,Category , SavePost ,Comment 

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import Profile , Follower

from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']




class ProfileSerializer(ModelSerializer):
    user  = UserSerializer()
    class Meta:
        model = Profile
        fields = ["user" , "picture", "bio" , "location"]



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name" ,"user" ,"slug","parent","description", "get_absolute_url"]




class PostSerializer(ModelSerializer):
    categories = CategorySerializer(read_only = True , many = True)
    user  = UserSerializer()
    comments = serializers.StringRelatedField(many = True)
    like = serializers.StringRelatedField(many = True)
    class Meta:
        model = Post
        fields = ["title" ,"thumbnail" ,"description","updated" ,"user" ,
            "voice" ,"created", "categories" ,"likes", 
            "status" ,"get_absolute_url" ,'comments',"like"]


class CommentSerializer(ModelSerializer):
    post  = PostSerializer()
    user  = UserSerializer()
    class Meta:
        model = Comment
        fields = ['body', 'user' , 'parent' , 'post']



class savepostSerializer(ModelSerializer):
    
    user = UserSerializer()
    saved_post =PostSerializer()
    class Meta:
        model = SavePost
        fields = ["user" , "saved_post", 'time' ]

