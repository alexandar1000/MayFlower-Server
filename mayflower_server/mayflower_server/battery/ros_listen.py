'''
Responsible for the connection with ROS regarding the incoming battery power readings
'''
from __future__ import print_function
from mayflower_server.battery.models import Battery
from mayflower_server.ros_tools import subscriber, connector
import logging

logger = logging.getLogger(__name__)

class RosBatteryListener(subscriber.RosSubscriber):
    '''
    Responsible for the connection with ROS regarding the incoming battery data readings
    '''
    def __init__(self):
        super().__init__()
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/battery',
                message_type='sensor_msgs/BatteryState',
                callback_function=self.receive_battery_reading
            )
        except Exception:
            logger.error("Error while subscribing to the battery topic")
            raise


    def receive_battery_reading(self, batteryData):
        '''
        Accept the incoming battery data reading
        '''
        if connector.RosConnector.is_connected():
            percentage = round(batteryData['percentage'], 5)
            battery = Battery(percentage=percentage, header_secs=batteryData['header']['stamp']['secs'])
            status = batteryData['power_supply_status']
            dataStr = ""
            if(status == 0):
                dataStr = "UNKNOWN"
            elif(status == 1):
                dataStr = "CHARGING"
            elif(status == 2):
                dataStr = "DISCHARGING"
            elif(status == 3):
                dataStr = "NOT_CHARGING"
            elif(status == 4):
                dataStr = "FULL"
            battery.power_supply_status = dataStr
            battery.save()
