from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import (
    UserRegistration,
    UserUpdate,
    UserLogin
    )

urlpatterns = [
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path('registration/',UserRegistration.as_view() , name= 'user-register'),
    path('login/',UserLogin.as_view() , name= 'user-login'),
    path('update/',UserUpdate.as_view() , name= 'profile-update')
]