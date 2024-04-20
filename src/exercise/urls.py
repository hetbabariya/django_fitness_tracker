from django.urls import path

from exercise.views import (
    CreateExerciseView,
    DeleteExerciseView,
    GetAllExerciseView,
    UpdateExerciseView
    )

urlpatterns=[
    path('create/',CreateExerciseView.as_view()),
    path('update/',UpdateExerciseView.as_view()),
    path('delete/<int:id>',DeleteExerciseView.as_view()),
    path('',GetAllExerciseView.as_view())
]