from django.urls import include, path
from .views import (
    UserRegistration
    )

urlpatterns = [
    path('registration/',UserRegistration.as_view())
]