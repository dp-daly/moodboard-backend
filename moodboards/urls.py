from django.urls import path
from .views import MoodboardListView, MoodboardDetailView

urlpatterns = [
    path('', MoodboardListView.as_view()),
    path('<int:pk>/', MoodboardDetailView.as_view())
]