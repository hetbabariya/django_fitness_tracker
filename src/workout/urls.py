from django.urls import path

from .views import (
    AllWorkoutsView,
    CreateWorkoutView,
    DeleteWorkoutView,
    EndWorkoutView,
    UpdateWorkoutView,
    WorkoutViweById,
    WorkoutViweByUserId
)

urlpatterns=[
    path('',AllWorkoutsView.as_view()),
    path('create/',CreateWorkoutView.as_view()),
    path('update/',UpdateWorkoutView.as_view()),
    path('delete/<int:id>/',DeleteWorkoutView.as_view()),
    path('<int:id>/',WorkoutViweById.as_view()),
    path('user/<int:id>/',WorkoutViweByUserId.as_view()),
    path('end/<int:id>/',EndWorkoutView.as_view()),
]