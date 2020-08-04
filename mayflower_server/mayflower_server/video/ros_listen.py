'''
Connection with ROS regarding the incoming video images
'''

from __future__ import print_function
from mayflower_server.video.models import Video
from mayflower_server.ros_tools import subscriber, connector


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
            image = Video(video_image=image)
            image.save()
