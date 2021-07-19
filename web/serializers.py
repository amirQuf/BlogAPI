from .models import Post ,Category , SavePost ,Comment 

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.serialzers import UserSerializer
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name" ,"user" ,"slug","parent","description", "get_absolute_url"]


class PostSerializer(ModelSerializer):
    categories = CategorySerializer(read_only = True , many = True)
    user  = UserSerializer(read_only = True)
    comments = serializers.StringRelatedField(many = True)
    like = serializers.StringRelatedField(many = True)
    class Meta:
        model = Post
        fields = ["title" ,"thumbnail" ,"description" ,"user" ,
            "voice" ,"created", "categories" ,"likes", 
            "status" ,"get_absolute_url" ,'comments',"like"]


class CommentSerializer(ModelSerializer):
    post  = PostSerializer(read_only = True)
    user  = UserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = ['body', 'user' , 'parent' , 'post']



class savepostSerializer(ModelSerializer):
    
    user = UserSerializer(read_only = True)
    saved_post =PostSerializer(read_only = True)
    class Meta:
        model = SavePost
        fields = ["user" , "saved_post", 'time' ]

