from rest_framework import serializers
from ..models import Moodboard

class MoodboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moodboard
        fields = '__all__'
