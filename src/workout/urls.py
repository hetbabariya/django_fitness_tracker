from django.urls import path

from .views import (
    AllWorkoutsView,
    CreateWorkoutView,
    DeleteWorkoutView,
    UpdateWorkoutView,
    WorkoutViweById,
    WorkoutViweByUserId
)

urlpatterns=[
    path('create/',CreateWorkoutView.as_view()),
    path('update/',UpdateWorkoutView.as_view()),
    path('delete/',DeleteWorkoutView.as_view()),
    path('<int:id>/',WorkoutViweById.as_view()),
    path('user/<int:id>/',WorkoutViweByUserId.as_view()),
    path('',AllWorkoutsView.as_view()),
]