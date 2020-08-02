import time
from datetime import datetime
# from mayflower_server import settings

import roslibpy

# client = roslibpy.Ros(host='localhost', port=9090)
# client.run()

# talker = roslibpy.Topic(client, '/chatter', 'std_msgs/String')

# while client.is_connected:
#     data = {'data': 'wasd'}
#     talker.publish(roslibpy.Message(data))
#     print('Sending message...', data)
#     time.sleep(1)

# talker.unadvertise()

# client.terminate()


class RosControlsPublisher:

    def __init__(self, ros_host='localhost', topic='/boat_controls'):
        self.host = ros_host
        self.port = 9090
        self.client = roslibpy.Ros(host=self.host, port=9090)
        self.client.run()
        self.talker = roslibpy.Topic(self.client, topic, 'std_msgs/String')

    def is_connected(self):
        if self.client.is_connected:
            return True
        return False

    def send_command(self, command):
        valid_commands = 'wasdWASD'
        if command not in valid_commands:
            return False

        if self.client.is_connected:
            data = {'data': command.lower()}
            self.talker.publish(roslibpy.Message(data))
            print(f'Message: "{data}" at {datetime.now()}')
            return True

    def disconnect(self):
        self.talker.unadvertise()
        self.client.terminate()
