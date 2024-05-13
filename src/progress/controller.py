from django.utils import timezone
from django.db.models import Sum
from rest_framework.views import Response
from progress.serializer import (
    CreateProgressSerializer,
    GetOneDayProgressSerializer,
    GetRangeProgressSerializer,
    UpdateProgressSerializer
    )
from exercise.models import Exercise
from progress.models import Progress
from workout.models import Workout
from rest_framework.exceptions import ValidationError


def create_progress(workout):
    try : 
        exercises = Exercise.objects.filter(workout=workout)
        total_duration = timezone.now() - workout.created_at   
        total_sets = exercises.aggregate(total_sets=Sum('sets'))['total_sets'] or 0
        total_reps = exercises.aggregate(total_reps=Sum('reps'))['total_reps'] or 0
        total_weight = exercises.aggregate(total_weight=Sum('weight'))['total_weight'] or 0

        data = {
            "workout": workout.id,
            "user": workout.user.id,
            "total_duration": total_duration.total_seconds()//60,
            "total_sets": total_sets,
            "total_reps": total_reps,
            "total_weight": total_weight
        }
        
        serializer = CreateProgressSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    
    
def update_progress(workout_id):
    workout = Workout.objects.get(pk=workout_id)
    
    if workout.is_ended:

        exercises = Exercise.objects.filter(workout=workout_id)
        total_sets = exercises.aggregate(total_sets=Sum('sets'))['total_sets']
        total_reps = exercises.aggregate(total_reps=Sum('reps'))['total_reps']
        total_weight = exercises.aggregate(total_weight=Sum('weight'))['total_weight']
        
        data = {
                "total_sets": total_sets,
                "total_reps": total_reps,
                "total_weight": total_weight
            }
        
        progress = Progress.objects.get(workout=workout_id)
        serializer = UpdateProgressSerializer(progress , data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        print("updated!")
        

def get_one_day_progress(request) : 
    
    try : 
        user = request.user.id
        serializer = GetOneDayProgressSerializer(data = request.data , context = {"user" : user} , partial = True)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=200)
    
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=403)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

def get_range_progress(request) : 
    
    try : 
        user = request.user.id
        serializer = GetRangeProgressSerializer(data = request.data , context = {"user" : user} , partial = True)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=200)
    
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=403)
    except Exception as e:
        return Response({"error": str(e)}, status=500)