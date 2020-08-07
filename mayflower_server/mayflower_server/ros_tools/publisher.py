'''
Handles ROS publishing
'''
import roslibpy
from .connector import RosConnector
class RosPublisher(RosConnector):
    '''
    Handles publishing of topics to ROS
    '''
    counter = 0
    publishers = {}

    def __init__(self):
        super().__init__()
        self.local_publishers = set()

    def publish_to_topic(self, topic, message_type):
        '''
        Publishes to a ROS topic and returns the subscription key
        '''
        publisher = roslibpy.Topic(self.get_client(), topic, message_type)
        RosPublisher.publishers[RosPublisher.counter] = publisher
        self.local_publishers.add(RosPublisher.counter)
        RosPublisher.counter += 1
        return RosPublisher.counter-1

    def unadvertise_from_topic(self, key):
        '''
        Unadvertise from a ROS topic given a subscription key
        '''
        try:
            RosPublisher.publishers[key].undavertise()
            RosPublisher.publishers.pop(key)
            self.local_publishers.remove(key)
        except KeyError:
            print("Invalid key for un-advertising")
            raise

    def publish_message(self, key, message):
        try:
            RosPublisher.publishers[key].publish(roslibpy.Message(message))
        except KeyError:
            print("Invalid key for publishing the message")
            raise

