from .common import ArtobjectSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedArtobjectSerializer(ArtobjectSerializer):
    owner = UserSerializer()