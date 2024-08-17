# from exercise.models import Exercise
# from workout.models import Workout
# from django.db.models import Sum
# from rest_framework import serializers


# def get_history_data(filter) :
#     workouts = Workout.objects.filter(filter)
        
#     if not workouts: 
#         raise serializers.ValidationError("No such workout exists for this user on the given date")
    
#     exercises = Exercise.objects.filter(workout__in=workouts)

#     # workout_data = GetWorkoutserializer(workouts, many=True)
#     # exercise_data = GetExerciseSerializer(exercises, many=True)
#     data = {}
#     for workout in workouts : 
#         data.update({})
#         print(workout.descriptions)
#         print(workout.is_ended)
#     # return {"workouts": workout_data.data, "exercises": exercise_data.data}