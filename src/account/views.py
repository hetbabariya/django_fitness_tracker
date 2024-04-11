from email import message
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account.controller import (
    auth_email, change_password, get_profile, reset_password, sent_auth_email, sent_reset_password_email, user_login, user_registration , update_user
    )



class UserRegistration(APIView):
    
    def post(self , request):
        
        message = user_registration(request)
        return message
    
class UserLogin(APIView):
    
    def post(self , request):
        message = user_login(request)
        return message
    
class UserUpdate(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def put(self,request):
        message = update_user(request)
        return message
    
class UserProfile(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        message = get_profile(request)
        return message
    
    
class UserChangePassword(APIView):
    Permission_class = [IsAuthenticated]
    
    def put(self , request):
        message = change_password(request)
        return message
    
class SentResetPassword(APIView):
    
    def post(self, request):
        message = sent_reset_password_email(request)
        return message
    
class  ResetPassword(APIView):
    
    def put(self, request , uid , token):
        message = reset_password(request , uid , token)
        return message
    
class SentAuthEmailView(APIView):

    def post(self, request):
        message = sent_auth_email(request)
        return message

class AuthEmailView(APIView):

    def post(self, request, uid, token):
        message = auth_email(request, uid, token)
        return message