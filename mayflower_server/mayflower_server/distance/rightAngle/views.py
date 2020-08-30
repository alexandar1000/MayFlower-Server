"""
Views for the distance package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.distance.rightAngle.models import RightAngleDistance
from mayflower_server.distance.rightAngle.serializers import RightAngleDistanceSerializer
from .ros_listen import RosRightAngleDistanceListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosRightAngleDistanceListener()

# Create your views here.
class RightAngleList(APIView):
    """
    List all distances, or create a new right angle distance reading.
    """
    def get(self, request):
        '''
        Return all the right_angle data entries.
        '''
        right_angle = RightAngleDistance.objects.all()
        serializer = RightAngleDistanceSerializer(right_angle, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new right_angle data entry.
        '''
        serializer = RightAngleDistanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid post request to right angle Distance endpoint")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RightAngleDetail(APIView):
    """
    Retrieve, update or delete a right angle data reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the right_angle_distance db object with the primary key primary_key.
        '''
        try:
            return RightAngleDistance.objects.get(pk=primary_key)
        except RightAngleDistance.DoesNotExist:
            logger.warning("Non-existing right angle distance requested from the server")
            raise Http404

    def get(self, request, primary_key):
        '''
        Return the right_angle_distance with the primary key primary_key.
        '''
        right_angle = self.get_object(primary_key)
        serializer = RightAngleDistanceSerializer(right_angle)
        return Response(serializer.data)

    def delete(self, request, primary_key):
        '''
        Delete the right_angle_distance with the primary key primary_key.
        '''
        right_angle = self.get_object(primary_key)
        right_angle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
