from rest_framework import serializers
from mayflower_server.distance.frontRight.models import FrontRightDistance


class FrontRightDistanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the FrontRightDistance model
    '''

    class Meta:
        model = FrontRightDistance
        fields = ['id', 'received_at', 'header_secs', 'distance']
