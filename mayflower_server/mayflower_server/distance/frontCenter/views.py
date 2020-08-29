"""
Views for the distance package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.distance.frontCenter.models import FrontCenterDistance
from mayflower_server.distance.frontCenter.serializers import FrontCenterDistanceSerializer
from .ros_listen import RosFrontCenterDistanceListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosFrontCenterDistanceListener()

# Create your views here.
class FrontCenterList(APIView):
    """
    List all distances, or create a new front center distance reading.
    """
    def get(self, request):
        '''
        Return all the front_center data entries.
        '''
        front_center = FrontCenterDistance.objects.all()
        serializer = FrontCenterDistanceSerializer(front_center, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new front_center data entry.
        '''
        serializer = FrontCenterDistanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid post request to Front Center Distance endpoint")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FrontCenterDetail(APIView):
    """
    Retrieve, update or delete a front center data reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the front_center_distance db object with the primary key primary_key.
        '''
        try:
            return FrontCenterDistance.objects.get(pk=primary_key)
        except FrontCenterDistance.DoesNotExist:
            logger.warning("Non-existing front center distance requested from the server")
            raise Http404

    def get(self, request, primary_key):
        '''
        Return the front_center_distance with the primary key primary_key.
        '''
        front_center = self.get_object(primary_key)
        serializer = FrontCenterDistanceSerializer(front_center)
        return Response(serializer.data)

    def delete(self, request, primary_key):
        '''
        Delete the front_center_distance with the primary key primary_key.
        '''
        front_center = self.get_object(primary_key)
        front_center.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
