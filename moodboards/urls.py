from django.urls import path
from .views import MoodboardListView, MoodboardDetailView, RemoveArtobjectFromMoodboardView

urlpatterns = [
    path('', MoodboardListView.as_view()),
    path('<int:pk>/', MoodboardDetailView.as_view()),
    path('<int:pk>/<int:artobject_id>/', RemoveArtobjectFromMoodboardView.as_view()),
]