from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import UserRegistrationSerializer
from account.controller import user_registration

class UserRegistration(APIView):
    
    def post(self , request):
        
        message = user_registration(request)
        return message