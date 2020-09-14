from rest_framework import serializers
from mayflower_server.distance.frontLeft.models import FrontLeftDistance


class FrontLeftDistanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the FrontLeftDistance model
    '''

    class Meta:
        model = FrontLeftDistance
        fields = ['id', 'received_at', 'header_secs', 'distance']
