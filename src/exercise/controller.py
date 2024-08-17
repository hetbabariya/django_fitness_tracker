from functools import partial
from multiprocessing import context
from rest_framework.exceptions import ValidationError
from exercise.serializer import CreateExerciseSerializer, DeleteExerciseSerializer, GetAllExerciseSerializer, GetExerciseByIdSerializer, UpdateExerciseSerializer
from rest_framework.views import Response

from exercise.models import Exercise
from progress.controller import update_progress



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

        workout_id = exercise.workout.id
        update_progress(workout_id)

        return Response({"message": "Exercise updated successfully"}, status=200)
    except Exercise.DoesNotExist:
        return Response({"error": "Exercise does not exist."}, status=404)
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

def delete_exercise(request , id):
    try:
        exercise = Exercise.objects.get(pk=id)
        workout_id = exercise.workout.id

        serializer = DeleteExerciseSerializer(data={'id' : id}, context={"user": request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.delete()

        update_progress(workout_id)

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


def get_exercise_by_id(request, id):
    try:
        user_id = request.user.id
        exercise = Exercise.objects.select_related('workout').get(pk=id)

        if exercise.workout.user_id != user_id:
            raise ValidationError("You are not the owner of this exercise.")

        serializer = GetExerciseByIdSerializer(instance=exercise, context={"user": user_id})
        return Response(serializer.data, status=200)

    except Exercise.DoesNotExist:
        return Response({"error": "Exercise does not exist."}, status=404)
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=403)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


def get_exercise_by_workout_id(request, id):
    try:
        user_id = request.user.id

        exercises = Exercise.objects.select_related('workout').filter(workout=id).order_by('created_at')

        if not exercises :
            raise ValidationError ({"error": "No exercises found for the given workout ID."})

        for exercise in exercises:
            if exercise.workout.user_id != user_id:
                raise ValidationError("You are not the owner of one or more exercises.")

        serializer = GetExerciseByIdSerializer(instance=exercises, context={"user": user_id}, many=True)
        return Response(serializer.data, status=200)

    except ValidationError as ve:
        return Response({"error": ve.detail}, status=403)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
