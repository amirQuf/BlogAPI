from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



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
    created = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 1 , choices = STATUS_CHOICES)
    def __str__(self):
        return f"{self.title}|{self.user.username}"
    class Meta:
        ordering = ['-updated']
        verbose_name = "پست"
        verbose_name_plural = " پست ها"

        

