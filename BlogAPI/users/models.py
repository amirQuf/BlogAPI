from django.db import models
from django.contrib.auth.models import User
from django_otp.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 1
    MEMBER = 2
    ROLES = (
        (ADMIN, "Admin"),
        (MEMBER, "member"),
    )
    email = models.EmailField(unique=True)
    role = models.SmallIntegerField(choices=ROLES, default=MEMBER)
    profile = models.ImageField(upload_to="user/profile")



class OTPVerification(TimeStampedModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='otp_verification'
    )
    otp_secret_key = models.CharField(max_length=16)
    is_verified = models.BooleanField(default=False)




