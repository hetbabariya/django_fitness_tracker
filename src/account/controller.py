from functools import partial
from account.models import CustomUser
from .serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserUpdateSerializer
    )
from rest_framework.views import Response
from django.contrib.auth import authenticate
from .utils import get_tokens_for_user

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