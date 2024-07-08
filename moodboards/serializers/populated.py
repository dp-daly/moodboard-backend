from .common import MoodboardSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedMoodboardSerializer(MoodboardSerializer):
    createdby = UserSerializer()