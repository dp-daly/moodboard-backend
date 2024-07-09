from rest_framework import serializers
from ..models import Moodboard
from artobjects.serializers.common import ArtobjectSerializer

class MoodboardSerializer(serializers.ModelSerializer):
        artobjects = ArtobjectSerializer(many=True, read_only=True)
        
        class Meta:
              model = Moodboard
              fields = '__all__'
