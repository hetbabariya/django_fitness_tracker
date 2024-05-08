from progress.models import Progress
from workout.models import Workout
from django.db.models import Sum
from rest_framework import serializers


def count_total_progress(user , filter) :
    workouts = Workout.objects.filter(filter)
        
    if not workouts: 
        raise serializers.ValidationError("No such workout exists for this user on the given date")
        
    for workout in workouts : 
        if user != workout.user.id : 
            raise serializers.ValidationError("This is not your workout")
    
    progresses = Progress.objects.filter(workout__in=workouts)

    aggregated_data = progresses.aggregate(
        total_duration=Sum('total_duration'),
        total_sets=Sum('total_sets'),
        total_reps=Sum('total_reps'),
        total_weight=Sum('total_weight')
    )
    
    return aggregated_data
        