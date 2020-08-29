"""
Views for the distance package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.distance.frontLeft.models import FrontLeftDistance
from mayflower_server.distance.frontLeft.serializers import FrontLeftDistanceSerializer
from .ros_listen import RosFrontLeftDistanceListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosFrontLeftDistanceListener()

# Create your views here.
class FrontLeftList(APIView):
    """
    List all distances, or create a new front left distance reading.
    """
    def get(self, request):
        '''
        Return all the front_left data entries.
        '''
        front_left = FrontLeftDistance.objects.all()
        serializer = FrontLeftDistanceSerializer(front_left, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new front_left data entry.
        '''
        serializer = FrontLeftDistanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid post request to Front Left Distance endpoint")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FrontLeftDetail(APIView):
    """
    Retrieve, update or delete a front left data reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the front_left_distance db object with the primary key primary_key.
        '''
        try:
            return FrontLeftDistance.objects.get(pk=primary_key)
        except FrontLeftDistance.DoesNotExist:
            logger.warning("Non-existing front left distance requested from the server")
            raise Http404

    def get(self, request, primary_key):
        '''
        Return the front_left_distance with the primary key primary_key.
        '''
        front_left = self.get_object(primary_key)
        serializer = FrontLeftDistanceSerializer(front_left)
        return Response(serializer.data)

    def delete(self, request, primary_key):
        '''
        Delete the front_left_distance with the primary key primary_key.
        '''
        front_left = self.get_object(primary_key)
        front_left.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
