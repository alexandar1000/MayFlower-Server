"""
Views for the battery package.
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.battery.models import Battery
from mayflower_server.battery.serializers import BatterySerializer
from .ros_listen import RosBatteryListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosBatteryListener()


class BatteryList(APIView):
    """
    List all battery, or create a new battery data reading.
    """

    def get(self, request):
        """
        Return all the battery entries.
        """
        battery = Battery.objects.all()
        serializer = BatterySerializer(battery, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Post a new battery entry.
        """
        serializer = BatterySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.warning("Invalid battery post request")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BatteryDetail(APIView):
    """
    Retrieve, update or delete a Battery reading.
    """

    def get_object(self, primary_key):
        """
        Retrieve the battery db object with the primary key primary_key.
        """
        try:
            return Battery.objects.get(pk=primary_key)
        except Battery.DoesNotExist:
            logger.error("Invalid battery data reading request")
            raise Http404

    def get(self, request, pk):
        """
        Return the battery with the primary key pk.
        """
        battery = self.get_object(pk)
        serializer = BatterySerializer(battery)
        return Response(serializer.data)

    def delete(self, request, pk):
        """
        Delete the battery with the primary key pk.
        """
        battery = self.get_object(pk)
        battery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        """
        Update the battery with the primary key pk
        """
        battery = self.get_object(pk)
        serializer = BatterySerializer(battery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.warning("Invalid battery put request")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
