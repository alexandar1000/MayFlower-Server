'''
Connection with ROS regarding the incoming front center distance
'''

from __future__ import print_function
from mayflower_server.distance.frontCenter.models import FrontCenterDistance
from mayflower_server.ros_tools import subscriber, connector
from django.core.files.base import ContentFile
import datetime
import logging

logger = logging.getLogger(__name__)

class RosFrontCenterDistanceListener(subscriber.RosSubscriber):

    '''
        Connection with ROS regarding the incoming front center distance
    '''

    def __init__(self):
        super().__init__()
        # front center laser
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/frontCenterLaser_',
                message_type='sensor_msgs/Range',
                callback_function=self.receive_frontCenter
            )
        except Exception:
            logger.error("Error while subscribing to frontCenterLaser_ topic")
            raise

    def receive_frontCenter(self, laserData):
        if connector.RosConnector.is_connected():
            try:
                frontCenter = FrontCenterDistance(distance=laserData['range'], header_secs=laserData['header']['stamp']['secs'])
                frontCenter.save()
            except Exception:
                logger.error("Error while saving the front center laser distance from ROS")
                raise
