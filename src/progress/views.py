from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from progress.controller import (
    get_one_day_progress,
    get_week_progress
    )

class GetOneDayProgressView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request) : 
        message = get_one_day_progress(request)
        return message

class GetWeekProgressView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request) : 
        message = get_week_progress(request)
        return message