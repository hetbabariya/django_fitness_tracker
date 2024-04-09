from rest_framework import serializers
from account.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta: 
        model = CustomUser
        
        fields = [
            'email',
            'password',
            'username',
            'first_name',
            'last_name',
            'age',
            'weight',
            'height',
            'gender'
        ]
                
    def create(self, validated_data):        
        user = CustomUser.objects.create_user(**validated_data)
        return user        

