from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)
    Category = models.ForeignKey('self', on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f"{self.name}|{self.user.username}"

class Post(models.Model):
    STATUS_CHOICES = (
        ('D','draft'),
        ('P','Publish'),
        )
    title = models.CharField(max_length = 200)
    thumbnail = models.ImageField(upload_to = 'post')
    description = models.TextField()
    updated = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User,  on_delete = models.CASCADE)
    voice = models.FileField(upload_to='voice-post',blank=True,null=True)
    created = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField(Category)
    status = models.CharField(max_length = 1 , choices = STATUS_CHOICES)
    def __str__(self):
        return f"{self.title}|{self.user.username}"
    class Meta:
        ordering = ('-updated',)
  

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"{self.body}|{self.user.username}"
    class Meta:
        ordering = ('-created',)
        


        

