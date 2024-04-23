from django.db import models

class ExerciseList(models.Model):
    exercise_type = models.CharField(max_length=100)

    def __str__(self):
        return self.exercise_type

class Exercise(models.Model):
    workout = models.ForeignKey("workout.Workout", on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey('exercise.ExerciseList', on_delete=models.CASCADE, related_name='exercise_instances')
    sets = models.PositiveIntegerField(default=1)
    reps = models.PositiveIntegerField(default=1)
    weight = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.workout} - {self.exercise} - Sets: {self.sets}, Reps: {self.reps}, Weight: {self.weight}"

    class Meta:
        ordering = ['-created_at']