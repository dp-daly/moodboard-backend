from rest_framework import serializers
from ..models import Artobject

class ArtobjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artobject
        fields = '__all__'
