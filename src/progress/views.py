from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from progress.controller import (
    get_one_day_progress,
    get_range_progress,
    )

class GetOneDayProgressView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request) : 
        message = get_one_day_progress(request)
        return message

class GetRangeProgressView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request) : 
        message = get_range_progress(request)
        return message