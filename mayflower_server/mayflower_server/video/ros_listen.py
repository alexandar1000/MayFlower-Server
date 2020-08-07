'''
Connection with ROS regarding the incoming video images
'''

from __future__ import print_function
from mayflower_server.video.models import VideoImage
from mayflower_server.ros_tools import subscriber, connector
from django.core.files.base import ContentFile
import datetime
import base64

class RosVideoImageListener(subscriber.RosSubscriber):

    '''
    Connection with ROS regarding the incoming video images
    '''
    def __init__(self):
        super().__init__()
        self.sub_number = self.subscribe_to_topic(
            topic='/video_feed',
            message_type='sensor_msgs/CompressedImage',
            callback_function=self.receive_image_reading
        )

    def receive_image_reading(self, image):
        if connector.RosConnector.is_connected():
            name = f'image_{datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")}.jpeg'
            base64_bytes = image['data'].encode('ascii')
            image_bytes = base64.b64decode(base64_bytes)

            img = VideoImage.objects.create()
            img.video_image.save(name, ContentFile(image_bytes), save=True)