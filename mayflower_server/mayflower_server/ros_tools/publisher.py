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

    # TODO: Adapt to the publisher
    def publish_to_topic(self, topic, message_type):
        '''
        Publishes to a ROS topic and returns the subscription key
        '''
        publisher = roslibpy.Topic(self.get_client(), topic, message_type)
        # publisher.subscribe()
        RosPublisher.publishers[RosPublisher.counter] = publisher
        self.local_publishers.add(RosPublisher.counter)
        RosPublisher.counter += 1
        return RosPublisher.counter-1

    def unadvertise_from_topic(self, key):
        '''
        Unadvertise from a ROS topic given a subscription key
        '''
        if key in self.local_publishers:
            RosPublisher.publishers[key].unsubscribe()
            RosPublisher.publishers.pop(key)
            self.local_publishers.remove(key)
            return True
        return False