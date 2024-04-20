from rest_framework.exceptions import ValidationError

from .models import Workout
from .serializers import CreateWorkoutSerializer, DeleteWorkoutSerializer, GetAllWorkoutSerializer, GetByIdWorkoutSerializer, UpdateWorkoutSerializer
from rest_framework.views import Response

def create_workout(request):
    try : 
        data = {"user" : request.user.id , "descriptions" : request.data.get('descriptions')}
        serializer = CreateWorkoutSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {"message": "Workout created successfully"},
            status=201
        )
    
    except Exception as e : 
        return  Response({"error": str(e)}, status=400)
    
def update_workout(request):
    try:
        user_id = request.user.id
        serializer = UpdateWorkoutSerializer(data = request.data ,  context={'user' : user_id})
        serializer.is_valid(raise_exception=True)
        
        return Response(
            {"message" : "Workout Updated"},
            status=200
        )
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=404)
    except Exception as e:
        return Response({"error" : str(e)},status=400)
    

def delete_workout(request , id):
    try:
        user_id = request.user.id
        serializer = DeleteWorkoutSerializer(data={'id' : id}, context={'user': user_id})
        serializer.is_valid(raise_exception=True)
        serializer.delete()
        
        return Response({"message": "Workout Deleted"}, status=200)
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

def  get_workout_by_id(id):
    try:
        workout = Workout.objects.get(pk = id)
        serializer = GetByIdWorkoutSerializer(workout)
        return Response(serializer.data , status=200)
        
    except  Workout.DoesNotExist:
        return Response({"error" :"No workout with this id"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
def  get_workout_by_user_id(id):
    try:
        workout = Workout.objects.filter(user_id = id).order_by('created_at')
        serializer = GetByIdWorkoutSerializer(workout , many = True)
        return Response(serializer.data , status=200)
        
    except  Workout.DoesNotExist:
        return Response({"error" :"No workout with this id"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
def get_all_workout():
    try:
        workouts = Workout.objects.order_by('created_at')
        serializer = GetAllWorkoutSerializer(workouts)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)