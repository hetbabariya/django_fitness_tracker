from account.models import CustomUser
from .serializers import (
    AuthSerializer,
    SentAuthSerializer,
    SentResetPasswordSerializer,   
    UserChangePasswordSerializer,
    UserLoginSerializer,
    UserPasswordResetSerializer,
    UserRegistrationSerializer,
    UserUpdateSerializer,
    UserProfileSerializer
    )
from rest_framework.views import Response
from django.contrib.auth import authenticate
from .utils import get_tokens_for_user
from rest_framework import serializers

def user_registration(request):
    try : 
        
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {
                "message" : "Registation successfuly.",
            },status=201
        )
    except Exception as e : 
        return  Response({"error": str(e)}, status=400)
    
def user_login(request):
    try:
        serializers = UserLoginSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        
        email = serializers.data.get('email')
        passwrod = serializers.data.get('password')
        
        user = authenticate(username=email, password=passwrod)

        if user:
            
            token = get_tokens_for_user(user)
            
            return Response(
                {
                    "message" : "User login successfully",
                    'token'   : token
                },status=200
            )
        else :
            raise Exception("email or password is incorrect")
    except Exception as e : 
        return  Response({"error": str(e)}, status=400)
    
    
    
def update_user(request):
    try:
        user_id = request.user.id
        user = CustomUser.objects.get(pk=user_id)
        serializers = UserUpdateSerializer(user, data=request.data , partial = True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({"message" : "Data has been updated"}, status=200)
    except CustomUser.DoesNotExist:
        return Response({'error': 'The user does not exist'}, status=404)
    except Exception as e : 
        return  Response({"error": str(e)}, status=400)
    
def get_profile(request):
    try:
        user_id = request.user.id
        user = CustomUser.objects.get(pk=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=200)
    except CustomUser.DoesNotExist:
        return Response({'error': 'The user does not exist'}, status=404)
    except Exception as e : 
        return  Response({"error": str(e)}, status=400)
    
def change_password(request):
    try:
        user = authenticate(email=request.user.email , password = request.data['old_password'])
        
        if user:
            serializer = UserChangePasswordSerializer(data=request.data , context = {"user" : request.user})
            serializer.is_valid(raise_exception=True)
            
            return Response(
                {
                    "message" : "Password Change Successfuly"
                },status=200
            )
        else:
            raise Exception("Old password does not match")
    except serializers.ValidationError:
        return Response(
            {
                "message": "new password and confirm password don't match",
                "status_code": 401,
            },
            status=401,
        )
    except Exception as e:
        return Response(
            {"message": f"{str(e)}", "status_code": 400},
            status=400,
        )
        
def sent_reset_password_email(request):
    try:
        serializer = SentResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "message": "password reset link send. please check your email."
            },
            status=200,
        )
    except Exception as e:
        return Response(
            {"message": f"{str(e)}", "status": "error", "status_code": 400},
            status=400,
        )
        
def reset_password(request,uid,token):
    try:
        serializer = UserPasswordResetSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "message": "password reset successfully.",
                "status": "success",
                "status_code": 200,
            },
            status=200,
        )
    except Exception as e:
        return Response(
            {"message": f"{str(e)}", "status": "error", "status_code": 400},
            status=400,
        )

def sent_auth_email(request):
    try:
        serializer = SentAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "message": "link sent successfully",
                "status": "success",
                "status_code": 200,
            },
            status=200,
        )

    except Exception as e:
        return Response(
            {"message": f"{str(e)}", "status": "error", "status_code": 400},
            status=400,
        )


def auth_email(request, uid, token):
    try:
        serializer = AuthSerializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "message": "account verified successfully",
                "status": "success",
                "status_code": 200,
            },
            status=200,
        )
    except CustomUser.DoesNotExist:
        return Response(
            {
                "message": "user not found",
                "status": "error",
                "status_code": 404,
            },
            status=404,
        )

    except serializers.ValidationError:
        return Response(
            {
                "message": "Token is not valid or expired",
                "status": "error",
                "status_code": 401,
            },
            status=401,
        )
    except Exception as e:
        return Response(
            {"message": f"{str(e)}", "status": "error", "status_code": 400},
            status=400,
        )