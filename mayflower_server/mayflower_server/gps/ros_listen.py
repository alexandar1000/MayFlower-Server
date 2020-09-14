'''
Connection with ROS regarding the incoming gps
'''

from __future__ import print_function
from mayflower_server.gps.models import GPS
from mayflower_server.ros_tools import subscriber, connector
import logging

logger = logging.getLogger(__name__)

class RosGPSListener(subscriber.RosSubscriber):

    '''
    Connection with ROS regarding the incoming gps
    '''
    def __init__(self):
        super().__init__()
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/gpsData',
                message_type='sensor_msgs/NavSatFix',
                callback_function=self.receive_gps
            )
        except Exception:
            logger.error("Error while subscribing to gpsData topic")
            raise

    def receive_gps(self, gpsData):
        if connector.RosConnector.is_connected():
            gps = GPS(header_secs=gpsData['header']['stamp']['secs'], latitude=gpsData['latitude'],
                      longitude=gpsData['longitude'], altitude=gpsData['altitude'])
            gps.save()
