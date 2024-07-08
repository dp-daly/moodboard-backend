from .common import ArtobjectSerializer
from moodboards.serializers.common import MoodboardSerializer

class PopulatedArtobjectSerializer(ArtobjectSerializer):
    moodboard = MoodboardSerializer()