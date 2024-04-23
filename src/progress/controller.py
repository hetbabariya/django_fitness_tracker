from django.utils import timezone
from django.db.models import Sum
from rest_framework.views import Response
from progress.serializer import CreateProgressSerializer
from exercise.models import Exercise
from progress.models import Progress


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
    
    
