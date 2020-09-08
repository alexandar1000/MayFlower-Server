from mayflower_server.gps.models import GPS
from mayflower_server.gps.serializers import GPSSerializer
from rest_framework import generics
from .ros_listen import RosGPSListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosGPSListener()

class GPSList(generics.ListCreateAPIView):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer


class GPSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPS.objects.all()
    serializer_class = GPSSerializer