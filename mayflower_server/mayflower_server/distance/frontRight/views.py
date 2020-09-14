"""
Views for the distance package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.distance.frontRight.models import FrontRightDistance
from mayflower_server.distance.frontRight.serializers import FrontRightDistanceSerializer
from .ros_listen import RosFrontRightDistanceListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosFrontRightDistanceListener()

# Create your views here.
class FrontRightList(APIView):
    """
    List all distances, or create a new front right distance reading.
    """
    def get(self, request):
        '''
        Return all the front_right data entries.
        '''
        front_right = FrontRightDistance.objects.all()
        serializer = FrontRightDistanceSerializer(front_right, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new front_right data entry.
        '''
        serializer = FrontRightDistanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid post request to Front Right Distance endpoint")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FrontRightDetail(APIView):
    """
    Retrieve, update or delete a front right data reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the front_right_distance db object with the primary key primary_key.
        '''
        try:
            return FrontRightDistance.objects.get(pk=primary_key)
        except FrontRightDistance.DoesNotExist:
            logger.warning("Non-existing front right distance requested from the server")
            raise Http404

    def get(self, request, pk):
        '''
        Return the front_right_distance with the primary key primary_key.
        '''
        front_right= self.get_object(pk)
        serializer = FrontRightDistanceSerializer(front_right)
        return Response(serializer.data)

    def delete(self, request, pk):
        '''
        Delete the front_right_distance with the primary key primary_key.
        '''
        front_right = self.get_object(pk)
        front_right.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
