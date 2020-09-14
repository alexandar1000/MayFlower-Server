from mayflower_server.gps.models import GPS
from mayflower_server.gps.serializers import GPSSerializer
from rest_framework import generics, filters
# import django_filters
# from url_filter.integrations.drf import DjangoFilterBackend
from .ros_listen import RosGPSListener
import logging

logger = logging.getLogger(__name__)
ros_client = RosGPSListener()


# class GPSFilter(django_filters.FilterSet):
#     min_header_secs = django_filters.NumberFilter(name="header_secs", lookup_type='gte')
#     max_header_secs = django_filters.NumberFilter(name="header_secs", lookup_type='lte')
#     class Meta:
#         model = GPS
#         fields = ['id', 'received_at', 'header_secs', 'latitude', 'longitude', 'altitude']


class GPSList(generics.ListCreateAPIView):
    """handles the GET and POST methods for a list view"""

    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
    # filter_backends = [DjangoFilterBackend]
    # filter_class = GPSFilter


class GPSDetail(generics.RetrieveUpdateDestroyAPIView):
    """handles the GET PUT DELETE methods for a single gps view"""

    queryset = GPS.objects.all()
    serializer_class = GPSSerializer
