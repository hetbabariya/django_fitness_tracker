from django.urls import path
from progress.views import (
    GetOneDayProgressView,
    GetWeekProgressView
    )

urlpatterns = [
    path('get-one-day/',GetOneDayProgressView.as_view()),
    path('get-one-week/',GetWeekProgressView.as_view())
]