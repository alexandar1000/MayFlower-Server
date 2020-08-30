'''
battery module serializer
'''
from rest_framework import serializers
from mayflower_server.battery.models import Battery

class BatterySerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the BatteryPower model
    '''
    class Meta:
        model = Battery
        fields = ['id', 'received_at', 'header_secs', 'percentage', 'power_supply_status']
