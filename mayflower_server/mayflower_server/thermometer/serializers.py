'''
thermometer module serializer
'''
from rest_framework import serializers
from mayflower_server.thermometer.models import Temperature

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the Temperature model
    '''
    class Meta:
        model = Temperature
        fields = ['id', 'header_secs', 'temperature', 'received_at']
