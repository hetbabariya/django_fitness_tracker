from django.db import models

class Workout(models.Model):
    user = models.ForeignKey("account.CustomUser", on_delete=models.CASCADE, related_name="workouts")
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    descriptions = models.CharField(max_length=2048, null=True, blank=True)
    is_ended = models.BooleanField(default=False)

    def __str__(self):
        return f"Workout {self.pk}"

    class Meta:
        ordering = ['created_at']