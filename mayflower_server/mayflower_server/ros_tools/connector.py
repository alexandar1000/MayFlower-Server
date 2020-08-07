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
            try:
                RosConnector.__client = roslibpy.Ros(host=self.host, port=self.port)
                RosConnector.__client.run()
            except Exception:
                print("RosConnector failed")
                raise


    @staticmethod
    def is_connected():
        '''
        Check if there is a connection to ROS
        '''
        return RosConnector.__client.is_connected


    def disconnect(self):
        '''
        Disconnect the ROS instance
        '''
        self.client.terminate()

    @staticmethod
    def get_client():
        '''
        Return the static client instance
        '''
        return RosConnector.__client