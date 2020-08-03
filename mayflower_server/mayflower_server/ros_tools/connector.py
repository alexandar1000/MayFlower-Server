'''
Connector utilities for the ROS communication
'''
import roslibpy
from django.conf import settings

class RosConnector():
    '''
    Handles the inital, global connection with ROS
    '''
    __client = None

    def __init__(self):
        self.host = settings.ROSBRIDGE_HOST_ADDRESS
        self.port = int(settings.ROSBRIDGE_HOST_PORT)
        if RosConnector.__client is None:
            RosConnector.__client = roslibpy.Ros(host=self.host, port=self.port)
            RosConnector.__client.run()


    @staticmethod
    def is_connected():
        '''
        Check if there is a connection to ROS
        '''
        if RosConnector.__client.is_connected:
            return True
        return False

    def disconnect(self):
        '''
        Disconnect the ROS instance
        '''
        # self.listener.unsubscribe()
        # self.client.terminate()

    @staticmethod
    def get_client():
        '''
        Return the static client instance
        '''
        return RosConnector.__client