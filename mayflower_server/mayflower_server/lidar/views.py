"""
Views for the lidar package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.lidar.models import Lidar3D
from mayflower_server.lidar.serializers import Lidar3DSerializer
from .ros_listen import RosLidar3DListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosLidar3DListener()

# Create your views here.
class Lidar3DList(APIView):
    """
    List all 3D lidars, or create a new lidar reading.
    """
    def get(self, request):
        '''
        Return all the lidar entries.
        '''
        lidars = Lidar3D.objects.all()
        serializer = Lidar3DSerializer(lidars, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new 3D lidar entry.
        '''
        serializer = Lidar3DSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid post request to 3D Lidar endpoint")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Lidar3DDetail(APIView):
    """
    Retrieve, update or delete a 3D Lidar reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the 3D lidar db object with the primary key primary_key.
        '''
        try:
            return Lidar3D.objects.get(pk=primary_key)
        except Lidar3D.DoesNotExist:
            logger.warning("Non-existing 3D Lidar requested from the server")
            raise Http404

    def get(self, request, pk):
        '''
        Return the 3D Lidar with the primary key primary_key.
        '''
        lidar = self.get_object(pk)
        serializer = Lidar3DSerializer(lidar)
        return Response(serializer.data)

    def delete(self, request, pk):
        '''
        Delete the 3D Lidar with the primary key primary_key.
        '''
        lidar = self.get_object(pk)
        lidar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
