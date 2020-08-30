'''
gps module serializer
'''
from rest_framework import serializers
from mayflower_server.gps.models import GPS

class GPSSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the GPS model
    '''
    class Meta:
        model = GPS
        fields = ['id', 'received_at', 'header_secs', 'latitude', 'longitude', 'altitude']