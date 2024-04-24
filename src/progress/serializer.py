from rest_framework import serializers
from progress.models import Progress

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