from rest_framework import serializers

from mayflower_server.controls.models import Control

class ControlsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('command', 'created_at')
        model = Control