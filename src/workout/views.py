from email import message
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .controller import (
    create_workout,
    delete_workout,
    get_all_workout,
    get_workout_by_id,
    get_workout_by_user_id,
    update_workout
)


class CreateWorkoutView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def post(self , request):
        message = create_workout(request)
        return message

class UpdateWorkoutView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def put(self , request):
        message = update_workout(request)
        return message
    
class DeleteWorkoutView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def delete(self , request):
        message = delete_workout(request)
        return message
    
class WorkoutViweById(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self ,request, id):
        message = get_workout_by_id(id)
        return message

class WorkoutViweByUserId(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self ,request, id):
        message = get_workout_by_user_id(id)
        return message


class AllWorkoutsView(APIView):
    
    def get(self , request):
        workouts = get_all_workout()
        return workouts
        
# TODO:
class EndWorkoutView(APIView):
    pass