'''
battery module serializer
'''
from rest_framework import serializers
from mayflower_server.battery.models import BatteryPower

class BatteryPowerSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the BatteryPower model
    '''
    class Meta:
        model = BatteryPower
        fields = ['id', 'battery_power']
