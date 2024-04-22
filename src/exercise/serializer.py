from os import write
from rest_framework import serializers

from exercise.models import Exercise
from workout.models import Workout

class CreateExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['sets', 'reps', 'weight', 'exercise', 'workout']
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def validate(self, attrs):
        instance = attrs.get('workout')
        user_id = self.context.get('user')
        workout_id = instance.__dict__
        workout = Workout.objects.get(pk=workout_id['id'])
        if workout.user.id != user_id :
            raise serializers.ValidationError("not own workout")
                    
        if workout.is_ended:
            raise serializers.ValidationError("Workout is ended")
        return attrs



class UpdateExerciseSerializer(serializers.ModelSerializer):
    e_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Exercise
        fields = ['sets', 'reps', 'weight', 'exercise', 'e_id']
        
    def validate(self, attrs):
        e_id = attrs.get('e_id')
        user_id = self.context.get('user').id
        
        exercise = Exercise.objects.select_related('workout').get(pk=e_id)

        if exercise.workout.user_id != user_id:
            raise serializers.ValidationError("You are not the owner of this exercise.")
                
        return attrs

class DeleteExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(write_only=True)
    
    class Meta : 
        fields = ['id']
            
    def validate(self, attrs):
        e_id = attrs.get('id')
        user_id = self.context.get('user')

        try : 
            Exercise.objects.get(pk=e_id) 
        except Exercise.DoesNotExist : 
            raise serializers.ValidationError("This exercise does not exist")
        
        exercise = Exercise.objects.select_related('workout').get(pk=e_id)

        if exercise.workout.user_id != user_id:
            raise serializers.ValidationError("You are not the owner of this exercise.")
                
        return attrs

    def delete(self):
        e_id = self.validated_data.get('id')
        exercise = Exercise.objects.get(pk=e_id)
        exercise.delete()
        
class GetAllExerciseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise
        fields = '__all__'

        

class GetExerciseByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

