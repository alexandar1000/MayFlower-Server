'''
Views for the battery package.
'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.battery.models import BatteryPower
from mayflower_server.battery.serializers import BatteryPowerSerializer
from .ros_listen import RosBatteryPowerListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosBatteryPowerListener()


class BatteryPowerList(APIView):
    """
    List all batteryPower, or create a new batteryPower reading.
    """
    def get(self, request):
        '''
        Return all the batteryPower entries.
        '''
        batteryPower = BatteryPower.objects.all()
        serializer = BatteryPowerSerializer(batteryPower, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new batteryPower entry.
        '''
        serializer = BatteryPowerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid battery power post request")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BatteryPowerDetail(APIView):
    """
    Retrieve, update or delete a BatteryPower reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the batteryPower db object with the primary key primary_key.
        '''
        try:
            return BatteryPower.objects.get(pk=primary_key)
        except BatteryPower.DoesNotExist:
            logger.error("Invalid battery power reading request")
            raise Http404

    def get(self, request, primary_key):
        '''
        Return the batteryPower with the primary key primary_key.
        '''
        batteryPower = self.get_object(primary_key)
        serializer = BatteryPowerSerializer(batteryPower)
        return Response(serializer.data)

    def delete(self, request, primary_key):
        '''
        Delete the batteryPower with the primary key primary_key.
        '''
        batteryPower = self.get_object(primary_key)
        batteryPower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
