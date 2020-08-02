from __future__ import print_function
from mayflower_server.thermometer.models import Temperature
import roslibpy


class RosTemperatureListener:
    def __init__(self, ros_host='localhost', topic='/temperature_reading'):
        self.host = ros_host
        self.port = 9090
        self.client = roslibpy.Ros(host=self.host, port=9090)
        self.client.run()
        self.listener = roslibpy.Topic(self.client, topic, 'std_msgs/Float64')
        self.listener.subscribe(self.receive_temperature_reading)

    def is_connected(self):
        if self.client.is_connected:
            return True
        return False

    def receive_temperature_reading(self, temperature_reading):
        if self.client.is_connected:
            t = Temperature(temperature=temperature_reading['data'])
            t.save()

    def disconnect(self):
        self.listener.unsubscribe()
        self.client.terminate()
