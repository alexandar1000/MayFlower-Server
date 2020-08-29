from rest_framework import serializers
from mayflower_server.video.models import VideoImage


class VideoFeedSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serializer for the Video Feed model
    '''
    class Meta:
        model = VideoImage
        fields = ['id', 'created_at', 'video_image']
