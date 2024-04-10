from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account.controller import (
    user_login, user_registration , update_user
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
    