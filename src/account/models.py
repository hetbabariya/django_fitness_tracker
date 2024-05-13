from pyexpat import model
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)    
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    gender_choices = [
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    ]
    
    username = models.CharField(unique=True, null=False , blank=False , max_length=50) 
    email = models.EmailField(unique=True , null=False , blank=False)
    age = models.PositiveIntegerField(default=0)
    weight = models.FloatField(help_text="Enter your weight in Kg", default=0)
    height = models.PositiveIntegerField(help_text="Enter your Height in cm", default=0)
    gender = models.CharField(max_length=6, choices=gender_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','age', 'weight', 'height', 'gender']
    
    def __str__(self):
        return f"{self.pk}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.is_superuser and not self.is_staff:
            self.is_staff = True
        super().save(*args, **kwargs)
