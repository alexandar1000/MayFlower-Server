'''
Responsible for the connection with ROS regarding the incoming temperature readings
'''
from __future__ import print_function
from mayflower_server.thermometer.models import Temperature
from mayflower_server.ros_tools import subscriber, connector
import logging
import time

logger = logging.getLogger(__name__)

class RosTemperatureListener(subscriber.RosSubscriber):
    '''
    Responsible for the connection with ROS regarding the incoming temperature readings
    '''
    def __init__(self):
        super().__init__()
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/temperature_reading',
                message_type='std_msgs/Float64',
                callback_function=self.receive_temperature_reading
            )
        except Exception:
            logger.error("Error while subscribing to temperature topic")
            raise


    def receive_temperature_reading(self, temperature_reading):
        '''
        Accept the incoming temperature reading
        '''
        if connector.RosConnector.is_connected():
            temperature = Temperature(header_secs=time.time(),
                                      temperature=temperature_reading['data'])
            temperature.save()
