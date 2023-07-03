from rest_framework import serializers, ModelSerializer

from users.serialzers import UserSerializer

from .models import Category, Comment, Post, SavePost


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name" ,"user" ,"slug","parent","description", "get_absolute_url"]


class OutputPostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only = True , many = True)
    user  = UserSerializer(read_only = True)
    comments = serializers.StringRelatedField(many = True)
    like = serializers.StringRelatedField(many = True)
    status = serializers.CharField(source="get_status_display")
    class Meta:
        model = Post
        fields = ["title" ,"thumbnail" ,"description" ,"user" ,
            "voice" ,"created", "categories" ,"likes", 
            "status" ,"get_absolute_url" ,'comments',"like"]



class InputPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title" ,"thumbnail" ,"description" ,"user" ,
            "voice" ,"created", "categories" ,"likes", 
            "status" ,"get_absolute_url" ,'comments',"like"]



class CommentSerializer(serializers.ModelSerializer):
    post  = OutputPostSerializer(read_only = True)
    user  = UserSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = ['body', 'user' , 'parent' , 'post']



class SavePostSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only = True)
    saved_post = OutputPostSerializer(read_only = True)
    class Meta:
        model = SavePost
        fields = ["user" , "saved_post", 'time' ]
