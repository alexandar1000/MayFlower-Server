import time
from datetime import datetime

import roslibpy

client = roslibpy.Ros(host='parallels', port=9090)
client.run()

talker = roslibpy.Topic(client, '/controls', 'std_msgs/String')

counter = 0

try:
    while client.is_connected:
        data = {'data': f'wasd {counter}'}
        counter += 1
        talker.publish(roslibpy.Message(data))
        print(f'{counter} - Sending message...', data)
        time.sleep(1)

except KeyboardInterrupt:
    talker.unadvertise()
    client.terminate()


# class RosControlsPublisher:
#
#     def __init__(self, ros_host='10.211.55.4', topic='/controls'):
#         self.host = ros_host
#         self.port = 9090
#         self.client = roslibpy.Ros(host=self.host, port=9090)
#         self.client.run()
#         self.talker = roslibpy.Topic(self.client, topic, 'std_msgs/String')
#         self.talker.advertise()
#
#     def is_connected(self):
#         if self.client.is_connected:
#             return True
#         return False
#
#     def send_command(self, command):
#         valid_commands = 'wasdWASD'
#         if command not in valid_commands:
#             return False
#
#         if self.client.is_connected:
#             data = {'data': command.lower()}
#             self.talker.publish(roslibpy.Message(data))
#             print(f'Message: "{data}" at {datetime.now()}')
#             return True
#
#     def disconnect(self):
#         self.talker.unadvertise()
#         self.client.terminate()
