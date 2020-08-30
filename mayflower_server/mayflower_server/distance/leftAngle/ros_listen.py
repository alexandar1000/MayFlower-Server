'''
Connection with ROS regarding the incoming left angle distance
'''

from __future__ import print_function
from mayflower_server.distance.leftAngle.models import LeftAngleDistance
from mayflower_server.ros_tools import subscriber, connector
import logging

logger = logging.getLogger(__name__)


class RosLeftAngleDistanceListener(subscriber.RosSubscriber):

    '''
        Connection with ROS regarding the incoming left angle distance
    '''

    def __init__(self):
        super().__init__()

        # left angle laser
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/leftAngleLaser_',
                message_type='sensor_msgs/Range',
                callback_function=self.receive_leftAngle
            )
        except Exception:
            logger.error("Error while subscribing to leftAngleLaser topic")
            raise

    def receive_leftAngle(self, laserData):
        if connector.RosConnector.is_connected():
            try:
                distance = ""
                if (laserData['range'] > 10):
                    distance = "> 10"
                else:
                    distance = str(laserData['range'])

                leftAngle = LeftAngleDistance(distance=distance, header_secs=laserData['header']['stamp']['secs'])
                leftAngle.save()
            except Exception:
                logger.error("Error while saving the left angle laser distance from ROS")
                raise
