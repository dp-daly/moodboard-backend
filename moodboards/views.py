from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import Moodboard
from .serializers.common import MoodboardSerializer
from .serializers.populated import PopulatedMoodboardSerializer


class MoodboardListView(APIView):

    def get(self, _request):
        moodboard = Moodboard.objects.all()
        serialized_moodboard = MoodboardSerializer(moodboard, many=True)
        return Response(serialized_moodboard.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        moodboard_to_add = MoodboardSerializer(data=request.data)
        try: 
            moodboard_to_add.is_valid()
            moodboard_to_add.save()
            return Response(moodboard_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e: 
            print("Error")
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
class MoodboardDetailView(APIView):
    
    def get_moodboard(self, pk):
        try:
            return Moodboard.objects.get(pk=pk)
        except Moodboard.DoesNotExist:
            raise NotFound(detail="Moodboard not found.")
    
    def get(self, _request, pk):
        moodboard = self.get_moodboard(pk=pk)
        serialized_moodboard = PopulatedMoodboardSerializer(moodboard)
        return Response(serialized_moodboard.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        moodboard_to_update = self.get_moodboard(pk=pk)
        updated_moodboard = MoodboardSerializer(moodboard_to_update, data=request.data)
        try:
            updated_moodboard.is_valid()
            updated_moodboard.save()
            return Response(updated_moodboard.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e: 
            return Response({ 'detail': str(e) }, 
                            status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def delete(self, _request, pk):
        moodboard_to_delete = self.get_moodboard(pk=pk)
        moodboard_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)