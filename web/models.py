from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    slug  = models.SlugField(unique=True,blank=True,null=True)
    parent = models.ForeignKey('self',blank=True,null=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"{self.name}|{self.user.username}"

    def get_absolute_url(self):
        return f"/cat/{self.slug}"


class Post(models.Model):
    STATUS_CHOICES = (
        ('D','draft'),
        ('P','Publish'),
        )

    title = models.CharField(max_length = 200)
    thumbnail = models.ImageField(upload_to = 'post')
    description = models.TextField()
    slug  = models.SlugField(unique = True ,blank=True,null=True)
    updated = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User,  on_delete = models.CASCADE)
    voice = models.FileField(upload_to = 'voice-post',blank=True,null=True)
    created = models.DateTimeField(auto_now_add = True)
    categories = models.ManyToManyField(Category,)
    likes = models.PositiveIntegerField(default = 0)
    status = models.CharField(max_length = 1 , choices = STATUS_CHOICES)

    def __str__(self):
        return f"{self.title}|{self.user.username}"

    def get_absolute_url(self):
        return f"/{self.user.username}/{self.slug}"
    
    class Meta:
        ordering = ('-updated','-created',)
  

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post ,related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self',blank=True,null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.body}|{self.user.username}"

    class Meta:
        ordering = ('-created',)


class Like (models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name= 'like',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
       return f"{self.user.username}|{self.post.title}"

    class Meta:
        ordering = ('-created',)


class SavePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    saved_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-time',)