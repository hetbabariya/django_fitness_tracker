from django.urls import path
from progress.views import (
    GetOneDayProgressView,
    GetRangeProgressView,
    )

urlpatterns = [
    path('get-one-day/',GetOneDayProgressView.as_view()),
    path('get-range/',GetRangeProgressView.as_view())
]