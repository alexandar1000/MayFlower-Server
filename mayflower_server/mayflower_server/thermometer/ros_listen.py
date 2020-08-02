'''
Responsible for the connection with ROS regarding the incoming temperature readings
'''
from __future__ import print_function
import roslibpy
from mayflower_server.thermometer.models import Temperature


class RosTemperatureListener:
    '''
    Responsible for the connection with ROS regarding the incoming temperature readings
    '''
    def __init__(self, ros_host='localhost', topic='/temperature_reading'):
        self.host = ros_host
        self.port = 9090
        self.client = roslibpy.Ros(host=self.host, port=9090)
        self.client.run()
        self.listener = roslibpy.Topic(self.client, topic, 'std_msgs/Float64')
        self.listener.subscribe(self.receive_temperature_reading)

    def is_connected(self):
        '''
        Check if there is a connection to ROS
        '''
        if self.client.is_connected:
            return True
        return False

    def receive_temperature_reading(self, temperature_reading):
        '''
        Accept the incoming temperature reading
        '''
        if self.client.is_connected:
            temperature = Temperature(temperature=temperature_reading['data'])
            temperature.save()

    def disconnect(self):
        '''
        Disconnect the ROS instance
        '''
        self.listener.unsubscribe()
        self.client.terminate()
