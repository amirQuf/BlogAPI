from users.models import User, OTPVerification 
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
import pyotp
import time
from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model

class UserSerializer(ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']





 class GenerateOTPSerializer(serializers.Serializer):
        email = serializers .EmailField()
        class Meta:
            model = User
            fields = ["email",]
        
        def validate(self, attrs):
            email = attrs.get("email").first()
            user = User.object.get(email=email)

            if user:
                otp_secret_key = pyotp.random_base32()
                # Save OTP secret key and associate with the user
                OTPVerification.objects.update_or_create(
                    user = User,
                    defaults={'otp_secret_key': otp_secret_key}
                    )
                # Generate OTP
                otp = pyotp.TOTP(otp_secret_key)
                otp_value = otp.now()
                #sending OTP by email
                subject = 'Subject'
                message = f'otp:{otp_value}'
                send_mail(
                subject,
                'Message body',
                User.email,
                    )
            else:
                raise ValidationError("email is not exist.")
            return attrs

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=False)
    password = serializers.CharField(max_length = 128)
    otp = serializers.CharField(max_length = 8)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = User.object.get(email = email).first()
        if user:
            otp_verification = OTPVerification.objects.get(user = user)
            otp_secret_key = otp_verification.otp_secret_key
            otp = pyotp.TOTP(otp_secret_key)
            if otp.verify(otp):
                otp_verification.is_verified = True
                otp_verification.save()
                user = authenticate(email = email, password=password)
        else:
            raise ValidationError("user is not exist.")
        return attrs
