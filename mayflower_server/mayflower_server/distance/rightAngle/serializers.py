from rest_framework import serializers
from mayflower_server.distance.rightAngle.models import RightAngleDistance


class RightAngleDistanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the RightAngleDistance model
    '''

    class Meta:
        model = RightAngleDistance
        fields = ['id', 'received_at', 'header_secs', 'distance']
