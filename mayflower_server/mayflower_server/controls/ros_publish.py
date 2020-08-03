from datetime import datetime
from ..ros_tools.publisher import RosPublisher

import roslibpy

class RosControlPublisher(RosPublisher):

    def __init__(self, topic='/boat_controls'):
        super().__init__()
        self.message_type = 'std_msgs/String'
        self.talker = self.publish_to_topic(topic, self.message_type)
        self.publishers[self.talker].advertise()

    def send_command(self, command):
        valid_commands = 'wasdWASD'
        if command not in valid_commands:
            return False

        if self.is_connected():
            data = {'data': command.lower()}
            self.publishers[self.talker].publish(roslibpy.Message(data))
            print(f'Message: "{data}" at {datetime.now()}')
            return True

    def terminate_topic(self):
        return self.unadvertise_from_topic(self.talker)
