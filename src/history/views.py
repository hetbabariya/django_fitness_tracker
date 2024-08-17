from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , IsAdminUser

from history.controller import get_range_of_history

class GetHistoryView(APIView) : 

    permission_classes = [IsAuthenticated]
    
    def get(self , request) : 
        message = get_range_of_history(request)
        return message
    