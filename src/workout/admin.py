from django.contrib import admin

from .models import Workout

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['id','user_id','created_at','updated_at','is_ended','descriptions']
    list_filter = ['created_at','user_id']
    list_per_page = 10