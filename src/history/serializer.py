# serializer.py

from rest_framework import serializers
from exercise.models import Exercise
from workout.models import Workout
from django.db.models import Q 

        
class GetExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = ['sets', 'reps', 'weight', 'exercise_name']
        
    def get_exercise_name(self, instance):
        return instance.exercise.exercise_type
    
class GetWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['descriptions', 'is_ended']

class GetHistorySerializer(serializers.Serializer):
    start_date = serializers.DateField(write_only=True)
    end_date = serializers.DateField(write_only=True)
    data = serializers.SerializerMethodField()
    
    class Meta:
        fields = ['start_date', 'end_date', 'data']
    
    def get_data(self, obj):
        return obj
    
    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        
        if start_date > end_date:
            raise serializers.ValidationError("Start date cannot be after end date.")
        
        user = self.context.get('user')
        
        workout_filter = (
            Q(created_at__date__gte=start_date) & 
            Q(created_at__date__lte=end_date) & 
            Q(user=user)
        )
        
        workouts = Workout.objects.filter(workout_filter)
        
        if not workouts: 
            raise serializers.ValidationError("No workouts found for this user within the given date range.")
        

        serialized_workouts = []
        for workout in workouts:
            exercises = Exercise.objects.filter(workout=workout)
            workout_data = GetWorkoutSerializer(workout).data
            exercise_data = GetExerciseSerializer(exercises, many=True).data
            serialized_workouts.append({
                f"{workout}": workout_data,
                "exercises": exercise_data
            })
        return serialized_workouts
