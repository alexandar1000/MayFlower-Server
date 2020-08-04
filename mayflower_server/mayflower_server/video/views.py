"""
Views for the video feed package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from mayflower_server.video.models import Video
from mayflower_server.video.serializers import VideoFeedSerializer
from .ros_listen import RosVideoImageListener

ros_client = RosVideoImageListener()

# Create your views here.
class VideoFeedList(APIView):
    """
    List all temeratures, or create a new temperature reading.
    """
    def get(self, request):
        '''
        Return all the video_reading entries.
        '''
        video_image = Video.objects.all()
        serializer = VideoFeedSerializer(video_image, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        Post a new video_reading entry.
        '''
        serializer = VideoFeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VideoFeedDetail(APIView):
    """
    Retrieve, update or delete a temperature reading.
    """

    def get_object(self, primary_key):
        '''
        Retrieve the video_reading db object with the primary key primary_key.
        '''
        try:
            return Video.objects.get(pk=primary_key)
        except Video.DoesNotExist:
            raise Http404

    def get(self, request, primary_key):
        '''
        Return the video_reading with the primary key primary_key.
        '''
        video_image = self.get_object(primary_key)
        serializer = VideoFeedSerializer(video_image)
        return Response(serializer.data)

    def delete(self, request, primary_key):
        '''
        Delete the video_reading with the primary key primary_key.
        '''
        video_image = self.get_object(primary_key)
        video_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
