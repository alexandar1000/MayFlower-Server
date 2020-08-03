from rest_framework import serializers

from mayflower_server.controls import models

class ControlsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('command', 'created_at')
        model = models.Control