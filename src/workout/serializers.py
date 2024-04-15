from dataclasses import field
from pyexpat import model
from django.forms import ValidationError
from rest_framework import serializers

from .models import Workout

class CreateWorkoutSerializer(serializers.ModelSerializer):
    class Meta :
        model = Workout
        fields = ['user','descriptions']
        
    def create(self, validated_data):
        return super().create(validated_data)
    

class UpdateWorkoutSerializer(serializers.ModelSerializer):
    w_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Workout
        fields = ['w_id', 'descriptions']
        
    def validate(self, attrs):
        w_id = attrs.get('w_id')
        descriptions = attrs.get('descriptions')
        user_id = self.context.get('user')
        
        workout = Workout.objects.filter(pk=w_id, user=user_id).first()
        if workout:
            workout.descriptions = descriptions
            workout.save()
            return attrs
        else:
            raise serializers.ValidationError("User is not the owner of this workout")


class DeleteWorkoutSerializer(serializers.ModelSerializer):
    w_id = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        w_id = attrs.get('w_id')
        user_id = self.context.get('user')
        
        workout = Workout.objects.filter(pk=w_id, user=user_id).first()
        if not workout:
            raise serializers.ValidationError("User is not the owner of this workout")
        
        return attrs

    def delete(self):
        w_id = self.validated_data.get('w_id')
        workout = Workout.objects.get(pk=w_id)
        workout.delete()

class GetByIdWorkoutSerializer(serializers.ModelSerializer):    
    class Meta : 
        model = Workout
        fields = [
            'user_id',
            'created_at',
            'ended_at',
            'updated_at',
            'descriptions',
            'is_ended',
        ]

class GetAllWorkoutSerializer(serializers.ListSerializer):
    child = GetByIdWorkoutSerializer(read_only=True)
