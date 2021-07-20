from django.db import models
from django.contrib.auth.models import User




# class User(AbstractUser):
#     phone  = models .CharField(max_length = 11)
    



class Profile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    picture = models.ImageField( default = 'default.jpg',upload_to = 'profile-users' )
    phone  = models .CharField(max_length = 11, blank = True, null = True)
    bio  = models.CharField(max_length = 150, blank = True, null = True)
    location = models.CharField(max_length = 150, blank = True, null = True)
    is_vertified  = models.BooleanField(default=False ,blank = True, null = True)
    
    def __str__(self):
        return f"profile/{self.user.username}"


class Follower(models.Model):
    user = models.OneToOneField(User, related_name = 'user' , on_delete = models.CASCADE)
    following = models.ManyToManyField(User,related_name = "followings" )
   
    def __str__(self):
        return f"following list/{self.user.username}"


# class Asosication(models.Model):
#     name  = models.CharField(max_length=100)
#     user =