from django.urls import path

from history.views import GetHistoryView

urlpatterns = [
    path('get-range/',GetHistoryView.as_view()),
]