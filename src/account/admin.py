from turtle import update
from django.contrib import admin
from account.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','full_name','email','is_staff', 'is_active','updated_at','is_verified']
    list_editable = ['is_staff', 'is_active']
    search_fields = ('username',)   