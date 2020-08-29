from rest_framework import serializers
from mayflower_server.distance.frontCenter.models import FrontCenterDistance


class FrontCenterDistanceSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the FrontCenterDistance model
    '''

    class Meta:
        model = FrontCenterDistance
        fields = ['id', 'received_at', 'header_secs', 'distance']
