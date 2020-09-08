"""
Views for the distance package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.distance.leftAngle.models import LeftAngleDistance
from mayflower_server.distance.leftAngle.serializers import LeftAngleDistanceSerializer
from .ros_listen import RosLeftAngleDistanceListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosLeftAngleDistanceListener()


# Create your views here.
class LeftAngleList(APIView):
    """
    List all distances, or create a new left angle distance reading.
    """
    def get(self, request):
        '''
        Return all the left_angle data entries.
        '''
        left_angle = LeftAngleDistance.objects.all()
        serializer = LeftAngleDistanceSerializer(left_angle, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new left_angle data entry.
        '''
        serializer = LeftAngleDistanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid post request to left angle distance endpoint")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeftAngleDetail(APIView):
    """
    Retrieve, update or delete a left angle data reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the left_angle_distance db object with the primary key primary_key.
        '''
        try:
            return LeftAngleDistance.objects.get(pk=primary_key)
        except LeftAngleDistance.DoesNotExist:
            logger.warning("Non-existing left angle distance requested from the server")
            raise Http404

    def get(self, request, pk):
        '''
        Return the left_angle_distance with the primary key primary_key.
        '''
        left_angle = self.get_object(pk)
        serializer = LeftAngleDistanceSerializer(left_angle)
        return Response(serializer.data)

    def delete(self, request, pk):
        '''
        Delete the left_angle_distance with the primary key primary_key.
        '''
        left_angle = self.get_object(pk)
        left_angle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
