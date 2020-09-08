'''
Views for the gps package.
'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.gps.models import GPS
from mayflower_server.gps.serializers import GPSSerializer
from .ros_listen import RosGPSListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosGPSListener()


class GPSList(APIView):
    """
    List all temeratures, or create a new GPS reading.
    """
    def get(self, request):
        '''
        Return all the gps entries.
        '''
        gps = GPS.objects.all()
        serializer = GPSSerializer(gps, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new gps entry.
        '''
        serializer = GPSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid gps post request")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GPSDetail(APIView):
    """
    Retrieve, update or delete a gps reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the gps db object with the primary key primary_key.
        '''
        try:
            return GPS.objects.get(pk=primary_key)
        except GPS.DoesNotExist:
            logger.error("Invalid GPS reading request")
            raise Http404

    def get(self, request, pk):
        '''
        Return the gps with the primary key primary_key.
        '''
        gps = self.get_object(pk)
        serializer = GPSSerializer(gps)
        return Response(serializer.data)

    def delete(self, request, pk):
        '''
        Delete the gps with the primary key primary_key.
        '''
        gps = self.get_object(pk)
        gps.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
