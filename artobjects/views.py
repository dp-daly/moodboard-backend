from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Artobject
from .serializers.common import ArtobjectSerializer
from .serializers.populated import PopulatedArtobjectSerializer

# Create your views here.
class ArtobjectListView(APIView):

    def get(self, _request):
        artobject = Artobject.objects.all()
        serialized_artobjects = ArtobjectSerializer(artobject, many=True)
        return Response(serialized_artobjects.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        artobject_to_add = ArtobjectSerializer(data=request.data)
        try: 
            artobject_to_add.is_valid()
            artobject_to_add.save()
            return Response(artobject_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e: 
            print("Error")
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ArtobjectDetailView(APIView):

    # def get_artobject(self, pk):
    #     try:
    #         return Artobject.objects.get(pk=pk)
    #     except Artobject.DoesNotExist:
    #         raise NotFound(detail="Art object not found.")

    # def get(self, _request, pk):
    #     artobject = self.get_artobject(pk=pk)
    #     serialized_artobject = PopulatedArtobjectSerializer(artobject)
    #     return Response(serialized_artobject.data, status=status.HTTP_200_OK)

    def get_artobject(self, pk):
        try:
            return Artobject.objects.get(pk=pk)
        except Artobject.DoesNotExist:
            raise NotFound(detail="Artobject not found.")

    def get(self, request, pk):
        artobject = self.get_artobject(pk=pk)
        serialized_artobject = PopulatedArtobjectSerializer(artobject)
        return Response(serialized_artobject.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        artobject_to_update = self.get_artobject(pk=pk)
        
        updated_artobject = ArtobjectSerializer(artobject_to_update, data=request.data)
        try:
            updated_artobject.is_valid()
            updated_artobject.save()
            return Response(updated_artobject.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e: 
            return Response({ 'detail': str(e) }, 
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, pk):
        artobject_to_delete = self.get_artobject(pk=pk)
        artobject_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)