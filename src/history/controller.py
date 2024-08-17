# controller.py

from rest_framework.exceptions import ValidationError
from rest_framework.views import Response

from history.serializer import GetHistorySerializer

def get_range_of_history(request):
    try:
        user = request.user.id
        serializer = GetHistorySerializer(data=request.data, context={"user": user})
        serializer.is_valid(raise_exception=True)
        history_data = serializer.data  # Access the validated data
        return Response(history_data, status=200)
    except ValidationError as ve:
        return Response({"error": ve.detail}, status=400)  # Bad request
    except Exception as e:
        return Response({"error": str(e)}, status=500)
