from rest_framework.exceptions import ValidationError
from exercise.serializer import CreateExerciseSerializer, DeleteExerciseSerializer, GetAllExerciseSerializer, UpdateExerciseSerializer
from rest_framework.views import Response

from exercise.models import Exercise



def create_exercise(request):
    try : 
        serializer = CreateExerciseSerializer(data=request.data , context = {'user' : request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {"message" : "Exercise  created successfully"},
            status=201
        )
        
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=400)
    except Exception as e : 
        return Response({"error" : str(e)})


def update_exercise(request):
    try:
        e_id = request.data.get('e_id')
        exercise = Exercise.objects.get(pk=e_id)
        serializer = UpdateExerciseSerializer(exercise, data=request.data, context={"user": request.user}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response({"message": "Exercise updated successfully"}, status=200)
    except Exercise.DoesNotExist:
        return Response({"error": "Exercise does not exist."}, status=404)
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

def delete_exercise(request , id):
    try:
        serializer = DeleteExerciseSerializer(data={'id' : id}, context={"user": request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.delete()
    
        return Response({"message": "Exercise deleted successfully"}, status=200)
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

def get_all_exercise(request):
    try : 
        exercises = Exercise.objects.all().order_by('created_at')
        serializer = GetAllExerciseSerializer(data=exercises , many = True)
        serializer.is_valid()
        
        return Response(serializer.data , status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    

    
            
    