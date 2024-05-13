from django.contrib import admin

from progress.models import Progress

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['total_duration','total_sets', 'total_reps', 'total_weight','user' , 'workout']