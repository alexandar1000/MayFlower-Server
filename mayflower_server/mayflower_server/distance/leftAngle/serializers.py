from rest_framework import serializers
from mayflower_server.distance.leftAngle.models import LeftAngleDistance


class LeftAngleDistanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the LeftAngleDistance model
    '''

    class Meta:
        model = LeftAngleDistance
        fields = ['id', 'received_at', 'header_secs', 'distance']
