from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile (models.Model):
    picture = models.ImageField(upload_to = 'profile-users')
    bio  = models.CharField(max_length= 150, blank=True, null=True)
    location = models.CharField(max_length= 150, blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return f"profile/{self.user.username}"
    
# class Group(models.Model):
#     name = models.CharField(max_length = 200)
#     # user = models.ManyToManyField(User)
#     def __str__(self):
#         return self.name