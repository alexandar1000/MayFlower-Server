'''
Responsible for the connection with ROS regarding the incoming IMU
'''
from __future__ import print_function
from mayflower_server.imu.models import IMU
from mayflower_server.ros_tools import subscriber, connector
import logging

logger = logging.getLogger(__name__)

class RosIMUListener(subscriber.RosSubscriber):
    '''
    Responsible for the connection with ROS regarding the incoming imu
    '''
    def __init__(self):
        super().__init__()
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/imuData',
                message_type='sensor_msgs/Imu',
                callback_function=self.receive_imuData
            )
        except Exception:
            logger.error("Error while subscribing to temperature topic")
            raise


    def receive_imuData(self, imuData):
        '''
        Accept the incoming IMU
        '''
        if connector.RosConnector.is_connected():
            orientation = imuData['orientation']
            angular_vel = imuData['angular_velocity']
            linear_accel = imuData['linear_acceleration']
            imu = IMU(header_secs=imuData['header']['stamp']['secs'], orient_x=orientation['x'],
                      orient_y=orientation['y'], orient_z=orientation['z'], orient_w=orientation['w'],
                      angular_velocity_roll=angular_vel['x'], angular_velocity_yaw=angular_vel['y'],
                      angular_velocity_pitch=angular_vel['z'], linear_acceleration_forward=linear_accel['x'],
                      linear_acceleration_up=linear_accel['y'] , linear_acceleration_left=linear_accel['z'])
            imu.save()
