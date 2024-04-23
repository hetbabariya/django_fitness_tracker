from django.db import models

class Progress(models.Model):
    user = models.ForeignKey("account.CustomUser", on_delete=models.CASCADE, related_name="progresses")
    workout = models.ForeignKey("workout.Workout", on_delete=models.CASCADE, related_name="progresses")
    total_duration = models.PositiveIntegerField(null=False, blank=False)
    total_sets = models.PositiveIntegerField(null=False, blank=False)
    total_reps = models.PositiveIntegerField(null=False, blank=False)
    total_weight = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f"Progress for {self.user} on {self.workout}"