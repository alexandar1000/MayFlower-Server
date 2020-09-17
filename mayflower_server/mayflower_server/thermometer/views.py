'''
Views for the thermometer package.
'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.thermometer.models import Temperature
from mayflower_server.thermometer.serializers import TemperatureSerializer
from .ros_listen import RosTemperatureListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosTemperatureListener()


class TemperatureList(APIView):
    """
    List all temeratures, or create a new temperature reading.
    """
    def get(self, request):
        '''
        Return all the temperature_reding entries.
        '''
        temperatures = Temperature.objects.all()
        serializer = TemperatureSerializer(temperatures, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new temperature_reding entry.
        '''
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid temperature reading post request")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TemperatureDetail(APIView):
    """
    Retrieve, update or delete a temperature reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the temperature_reding db object with the primary key primary_key.
        '''
        try:
            if primary_key == 0:
                return Temperature.objects.last()
            return Temperature.objects.get(pk=primary_key)
        except Temperature.DoesNotExist:
            logger.error("Invalid temperature reading request")
            raise Http404

    def get(self, request, pk):
        '''
        Return the temperature_reding with the primary key primary_key.
        '''
        temperature = self.get_object(pk)
        serializer = TemperatureSerializer(temperature)
        return Response(serializer.data)

    def delete(self, request, pk):
        '''
        Delete the temperature_reding with the primary key primary_key.
        '''
        temperature = self.get_object(pk)
        temperature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
