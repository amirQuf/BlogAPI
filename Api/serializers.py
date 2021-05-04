from web.models import Post ,Category , SavePost 
from rest_framework.serializers import ModelSerializer
from users.models import Profile , Follower
#serialzers for users
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user" , "picture", "bio" , "location")





#serializers for  web app 
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("title" ,"thumbnail" ,"description","updated" ,"user" ,
            "voice" ,"created", "categories" ,"likes", "status" )



class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name" ,"user" ,"slug","parent","description", )


class savepostSerializer(ModelSerializer):
    class Meta:
        model = SavePost
        fields = ( "user" , "saved_post", 'time' )

