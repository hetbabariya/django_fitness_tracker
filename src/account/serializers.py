from rest_framework import serializers
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from account.models import CustomUser
from account.utils import sent_email


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta: 
        model = CustomUser
        
        fields = [
            'email',
            'password',
            'username',
            'first_name',
            'last_name',
            'age',
            'weight',
            'height',
            'gender'
        ]
                
    def create(self, validated_data):        
        user = CustomUser.objects.create_user(**validated_data)
        return user  

class UserUpdateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "age",
            "weight",
            "height"
        ]
    
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta :
        model = CustomUser
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
            'weight',
            'height',
            'gender'
        ]
        
        
class UserChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True,max_length=255)
    confirm_password = serializers.CharField(write_only=True,max_length=255)
    
    class Meta:
        fields = ['new_password','confirm_password']
        
    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        user = self.context.get('user')
        
        if new_password != confirm_password : 
            raise serializers.ValidationError(
                "password and confirm password don't match"
            )
        user.set_password(new_password)
        user.save()
        return attrs
    
class SentResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    
    class Meta:
        fields=['email']
        
    def validate(self,attrs):
        email = attrs.get('email')
        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.email))
            token = PasswordResetTokenGenerator().make_token(user)
            link = "http://localhost:3000/api/user/verify/" + uid + "/" + token
            body = "Click Following Link To Reset Password " + link
            data = {"subject": "Reset Password", "body": body, "to_email": user.email}
            sent_email(data)
            return attrs
        else:
            raise Exception("user is not registered")
        
class UserPasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        max_length=255, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=255, write_only=True
    )

    class Meta:
        fields = ["new_password", "confirm_password"]

    def validate(self, attrs):
        try:
            password = attrs.get("new_password")
            confirm_password = attrs.get("confirm_password")
            uid = self.context.get("uid")
            token = self.context.get("token")
            if password != confirm_password:
                raise serializers.ValidationError(
                    "password and confirm password don't match"
                )

            email = smart_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(email=email)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise Exception("token is not valid or expired")
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise Exception("token is not valid or expired")
