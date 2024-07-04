from .common import MoodboardSerializer
from jwt_auth.serializers import UserSerializer
from artobjects.serializers.common import ArtobjectSerializer

class PopulatedMoodboardSerializer(MoodboardSerializer):
    artobjects = ArtobjectSerializer(many=True)
    createdby = UserSerializer()