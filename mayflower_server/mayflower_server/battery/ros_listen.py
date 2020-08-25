'''
Responsible for the connection with ROS regarding the incoming battery power readings
'''
from __future__ import print_function
from mayflower_server.battery.models import BatteryPower
from mayflower_server.ros_tools import subscriber, connector
import logging

logger = logging.getLogger(__name__)

class RosBatteryPowerListener(subscriber.RosSubscriber):
    '''
    Responsible for the connection with ROS regarding the incoming battery power readings
    '''
    def __init__(self):
        super().__init__()
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/batteryPower',
                message_type='std_msgs/Float64',
                callback_function=self.receive_batteryPower_reading
            )
        except Exception:
            logger.error("Error while subscribing to the batteryPower topic")
            raise


    def receive_batteryPower_reading(self, batteryPower):
        '''
        Accept the incoming battery power reading
        '''
        if connector.RosConnector.is_connected():
            batteryPower = BatteryPower(batteryPower=batteryPower['data'])
            batteryPower.save()
