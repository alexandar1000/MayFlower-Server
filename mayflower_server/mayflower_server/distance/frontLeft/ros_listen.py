'''
Connection with ROS regarding the incoming front left distance
'''

from __future__ import print_function
from mayflower_server.distance.frontLeft.models import FrontLeftDistance
from mayflower_server.ros_tools import subscriber, connector
from django.core.files.base import ContentFile
import datetime
import logging

logger = logging.getLogger(__name__)

class RosFrontLeftDistanceListener(subscriber.RosSubscriber):

    '''
        Connection with ROS regarding the incoming front left distance
    '''

    def __init__(self):
        super().__init__()

        # front left laser
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/frontLeftLaser_',
                message_type='sensor_msgs/Range',
                callback_function=self.receive_frontLeft
            )
        except Exception:
            logger.error("Error while subscribing to frontLeftLaser topic")
            raise

    def receive_frontLeft(self, laserData):
        if connector.RosConnector.is_connected():
            try:
                frontLeft = FrontLeftDistance(distance=laserData['range'], header_secs=laserData['header']['stamp']['secs'])
                frontLeft.save()
            except Exception:
                logger.error("Error while saving the front left laser distance from ROS")
                raise
