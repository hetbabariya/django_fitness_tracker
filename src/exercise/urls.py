from django.urls import path

from exercise.views import (
    CreateExerciseView,
    DeleteExerciseView,
    GetAllExerciseView,
    GetExerciseByIdView,
    GetExerciseByWorkoutIdView,
    UpdateExerciseView
    )

urlpatterns=[
    path('',GetAllExerciseView.as_view()),
    path('create/',CreateExerciseView.as_view()),
    path('update/',UpdateExerciseView.as_view()),
    path('delete/<int:id>',DeleteExerciseView.as_view()),
    path('get-by-id/<int:id>',GetExerciseByIdView.as_view()),
    path('get-by-workout-id/<int:id>',GetExerciseByWorkoutIdView.as_view()),
]