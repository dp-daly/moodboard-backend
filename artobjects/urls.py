from django.urls import path
from .views import ArtobjectListView, ArtobjectDetailView

urlpatterns = [
    path('', ArtobjectListView.as_view()),
    path('<int:pk>/', ArtobjectDetailView.as_view())
]