import os
from django.core.mail import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken

from config import Config

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def sent_email(data):
        email = EmailMessage(
            subject=data["subject"],
            body=data["body"],
            from_email=Config.EMAIL_FROM,
            to=[data["to_email"]],
        )
        email.send()