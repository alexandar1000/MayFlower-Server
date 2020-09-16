from mayflower_server.gps.models import GPS
from mayflower_server.gps.serializers import GPSSerializer
from .filters import GPSFilter
from rest_framework import generics, filters
from django_filters import rest_framework
from django.http import JsonResponse
import json
from .ros_listen import RosGPSListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosGPSListener()


class GPSList(generics.ListCreateAPIView):
    """handles the GET and POST methods for a list view"""

    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
    # filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter)
    # filter_class = GPSFilter
    # search_fields = ('max_header_secs', 'min_header_secs')


class GPSDetail(generics.RetrieveUpdateDestroyAPIView):
    """handles the GET PUT DELETE methods for a single gps view"""

    queryset = GPS.objects.all()
    serializer_class = GPSSerializer


def GPSConvert(request):
    """
    handles Unity coordinates (x, z) converting to GPS (latitude, longitude)
    """
    StartPoint = (940, 437)
    StartGPS = (53.38455701638842, -1.4595508575439455)
    EndPoint = (-1228, -787)
    EndGPS = (53.403750049393025, -1.4112067222595215)
    x_unit = (EndGPS[0] - StartGPS[0]) / (EndPoint[0] - StartPoint[0])
    z_unit = (EndGPS[1] - StartGPS[1]) / (EndPoint[1] - StartPoint[1])

    cord_x = 0
    cord_z = 0
    if request.method == "GET":
        cord_x = request.GET.get('cord_x', '')
        cord_z = request.GET.get('cord_z', '')
    # elif request.method == "POST":
    #     json_data = json.loads(request.body)

    lat = StartGPS[0] + (x_unit * (int(cord_x, base=10) - StartPoint[0]))
    lon = StartGPS[1] + (z_unit * (int(cord_z, base=10) - StartPoint[1]))
    data = {
        'latitude': lat,
        'longitude': lon
    }
    return JsonResponse(data)


