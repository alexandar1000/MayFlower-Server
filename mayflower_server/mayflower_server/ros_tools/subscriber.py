'''
Handles ROS subscribing
'''
import roslibpy
from .connector import RosConnector
class RosSubscriber(RosConnector):
    '''
    Handles subscribing to ROS topics
    '''
    counter = 0
    subscribers = {}

    def __init__(self):
        super().__init__()
        self.local_subscribers = set()

    def subscribe_to_topic(self, topic, message_type, callback_function):
        '''
        Subscribe to a ROS topic and pass a callback_function to be invoked when a message arrives
        '''
        listener = roslibpy.Topic(self.get_client(), topic, message_type)
        listener.subscribe(callback_function)
        RosSubscriber.subscribers[RosSubscriber.counter] = listener
        self.local_subscribers.add(RosSubscriber.counter)
        RosSubscriber.counter += 1
        return RosSubscriber.counter-1

    def unsubscribe_from_topic(self, key):
        '''
        Unsubscribe from a ROS topic given a subscription key
        '''
        try:
            RosSubscriber.subscribers[key].unsubscribe()
            RosSubscriber.subscribers.pop(key)
            self.local_subscribers.remove(key)
        except KeyError:
            print("Invalid key for un-subscribing from the topic")
            raise
