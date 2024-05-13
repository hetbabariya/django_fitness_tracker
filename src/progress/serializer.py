from datetime import timedelta
from rest_framework import serializers
from progress.models import Progress
from progress.utils import count_total_progress
from workout.models import Workout
from django.db.models import Q , Sum

class CreateProgressSerializer(serializers.ModelSerializer):
    class Meta :
        model = Progress
        fields = ['user','workout','total_duration','total_sets','total_reps','total_weight']
        
    def create(self, validated_data):
        return Progress.objects.create(**validated_data)
    
class UpdateProgressSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Progress
        fields=['total_sets', 'total_reps', 'total_weight']
        
class GetOneDayProgressSerializer(serializers.ModelSerializer):
    date = serializers.DateField(write_only = True)
    
    class Meta : 
        model = Progress
        fields=['total_duration','total_sets', 'total_reps', 'total_weight','date']
        
    def validate(self, attrs):
        date = attrs.get('date')
        user = self.context.get('user')
        
        workout_filter = (
            Q(created_at__date=date) &
            Q(user=user) &
            Q(is_ended = True))
        
        data = count_total_progress(user=user , filter=workout_filter)
        attrs.update(data)
        return attrs

class GetRangeProgressSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(write_only = True)
    end_date = serializers.DateField(write_only = True)
    
    class Meta : 
        model = Progress
        fields=['total_duration','total_sets', 'total_reps', 'total_weight','start_date','end_date']
        
    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        
        user = self.context.get('user')
        
        workout_filter = (
            Q(created_at__date__gte = start_date ) & 
            Q(created_at__date__lte = end_date) & 
            Q(user=user) &
            Q(is_ended = True)
        )
        
        data = count_total_progress(user=user , filter=workout_filter)
        attrs.update(data)
        return attrs