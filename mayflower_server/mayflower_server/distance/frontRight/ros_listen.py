'''
Connection with ROS regarding the incoming front right distance
'''

from __future__ import print_function
from mayflower_server.distance.frontRight.models import FrontRightDistance
from mayflower_server.ros_tools import subscriber, connector
from django.core.files.base import ContentFile
import datetime
import logging

logger = logging.getLogger(__name__)

class RosFrontRightDistanceListener(subscriber.RosSubscriber):

    '''
        Connection with ROS regarding the incoming front right distance
    '''

    def __init__(self):
        super().__init__()

        # front right laser
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/frontRightLaser_',
                message_type='sensor_msgs/Range',
                callback_function=self.receive_frontRight
            )
        except Exception:
            logger.error("Error while subscribing to frontRightLaser topic")
            raise

    def receive_frontRight(self, laserData):
        if connector.RosConnector.is_connected():
            try:
                frontRight = FrontRightDistance(distance=laserData['range'], header_secs=laserData['header']['stamp']['secs'])
                frontRight.save()
            except Exception:
                logger.error("Error while saving the front right laser distance from ROS")
                raise
