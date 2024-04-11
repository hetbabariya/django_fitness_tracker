from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import (
    ResetPassword,
    SentResetPassword,
    UserChangePassword,
    UserProfile,
    UserRegistration,
    UserUpdate,
    UserLogin
    )

urlpatterns = [
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path('registration/',UserRegistration.as_view() , name= 'user-register'),
    path('login/',UserLogin.as_view() , name= 'user-login'),
    path('update/',UserUpdate.as_view() , name= 'profile-update'),
    path('profile/',UserProfile.as_view() , name= 'profile-view'),
    path('change-password/',UserChangePassword.as_view() , name= 'change password'),
    path('sent-rest-password-link/',SentResetPassword.as_view() , name= 'sent reset password'),
    path('rest-password/<uid>/<token>',ResetPassword.as_view() , name= 'reset password')
]