from rest_framework import serializers
from mayflower_server.lidar.models import Lidar3D


class Lidar3DSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the Lidar3D model
    '''
    class Meta:
        model = Lidar3D
        fields = ['id', 'received_at', 'height', 'width', 'fields', 'is_bigendian', 'point_step', 'row_step', 'data', 'is_dense']
