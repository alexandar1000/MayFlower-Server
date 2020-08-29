'''
Connection with ROS regarding the incoming front left distance
'''

from __future__ import print_function
from mayflower_server.distance.rightAngle.models import RightAngleDistance
from mayflower_server.ros_tools import subscriber, connector
from django.core.files.base import ContentFile
import datetime
import logging

logger = logging.getLogger(__name__)

class RosRightAngleDistanceListener(subscriber.RosSubscriber):

    '''
        Connection with ROS regarding the incoming right angle distance
    '''

    def __init__(self):
        super().__init__()

        # right angle laser
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/RightAngleLaser_',
                message_type='sensor_msgs/Range',
                callback_function=self.receive_rightAngle
            )
        except Exception:
            logger.error("Error while subscribing to RightAngleLaser topic")
            raise

    def receive_rightAngle(self, laserData):
        if connector.RosConnector.is_connected():
            try:
                rightAngle = RightAngleDistance(distance=laserData['range'], header_secs=laserData['header']['stamp']['secs'])
                rightAngle.save()
            except Exception:
                logger.error("Error while saving the right angle laser distance from ROS")
                raise
