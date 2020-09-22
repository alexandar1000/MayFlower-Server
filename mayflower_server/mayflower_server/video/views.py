"""
Views for the video feed package
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.conf import settings
from mayflower_server.video.models import VideoImage
from mayflower_server.video.serializers import VideoFeedSerializer
from .ros_listen import RosVideoImageListener
from django.http import FileResponse, HttpResponse
import glob
import os
import logging
import base64

logger = logging.getLogger(__name__)
ros_client = RosVideoImageListener()

# Create your views here.
class VideoFeedList(APIView):
    """
    List all images, or create a new temperature reading.
    """
    def get(self, request):
        '''
        Return all the video_reading entries.
        '''
        video_image = VideoImage.objects.all()
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

        logger.warning("Invalid post request to video feed endpoint")
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
            return VideoImage.objects.get(pk=primary_key)
        except VideoImage.DoesNotExist:
            logger.warning("Non-existing video requested from the server")
            raise Http404

    def get(self, request, pk):
        '''
        Return the video_reading with the primary key primary_key.
        '''
        video_image = self.get_object(pk)
        serializer = VideoFeedSerializer(video_image)
        return Response(serializer.data)

    def delete(self, request, pk):
        '''
        Delete the video_reading with the primary key primary_key.
        '''
        video_image = self.get_object(pk)
        video_image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageFeedDetail(APIView):
    '''
    Retrieve the newest image from the database
    '''

    def get(self, request):
        path = f'{settings.BASE_DIR}/video_images'
        # files = os.listdir(path)
        # paths = [os.path.join(path, basename) for basename in files]

        # latest_file = max(paths, key=os.path.getctime)
        latest_file = max(glob.glob(f'{path}/*.jpg'), key=os.path.getmtime)
        try:
            img = open(latest_file, 'rb').read()
            img_string = base64.b64encode(img).decode('utf-8')
            # response = FileResponse(img)
            return HttpResponse(img_string)


            # return response
        except FileNotFoundError:
            logger.error("No image found to retrieve")
            raise Http404