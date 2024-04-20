from django.contrib import admin

from exercise.models import Exercise, ExerciseList

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['workout' , 'exercise' , 'sets' , 'reps' , 'weight' , 'created_at' , 'updated_at']

@admin.register(ExerciseList)
class ExerciseListAdmin(admin.ModelAdmin):
    list_display = ['id','exercise_type']
    list_per_page = 10