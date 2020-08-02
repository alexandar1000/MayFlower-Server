from mayflower_server.thermometer.models import Temperature
from rest_framework import serializers

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ['id', 'temperature']