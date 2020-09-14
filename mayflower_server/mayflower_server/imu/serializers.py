'''
 imu module serializer
'''
from rest_framework import serializers
from mayflower_server.imu.models import IMU

class IMUSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the IMU model
    '''
    class Meta:
        model = IMU
        fields = ['id', 'received_at', 'header_secs', 'orient_x', 'orient_y', 'orient_z', 'orient_w',
                  'angular_velocity_roll', 'angular_velocity_yaw', 'angular_velocity_pitch', 'linear_acceleration_forward',
                  'linear_acceleration_up' ,'linear_acceleration_left']
