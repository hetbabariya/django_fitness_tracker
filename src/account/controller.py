from .serializers import UserRegistrationSerializer
from rest_framework.views import Response

def user_registration(request):
    try : 
        
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {
                "message" : "Registation successfuly.",
            },status=201
        )
    except Exception as e : 
        return  Response({"error": str(e)}, status=400)