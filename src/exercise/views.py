from exercise.controller import create_exercise, delete_exercise, get_all_exercise, update_exercise
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated , IsAdminUser

class CreateExerciseView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        message = create_exercise(request)
        return message
    
class UpdateExerciseView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def put(self , requset):
        message = update_exercise(requset)
        return message
    
class DeleteExerciseView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def delete(self , requset , id):
        message = delete_exercise(requset , id)
        return message
        
class GetAllExerciseView(APIView):
    
    permission_classes = [IsAdminUser]
    
    def get(self , requset):
        message = get_all_exercise(requset)
        return  message  