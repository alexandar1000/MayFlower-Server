'''
Connection with ROS regarding the incoming 3D lidar data
'''

from __future__ import print_function
from mayflower_server.lidar.models import Lidar3D
from mayflower_server.ros_tools import subscriber, connector
from django.core.files.base import ContentFile
import datetime
import logging


logger = logging.getLogger(__name__)

class RosLidar3DListener(subscriber.RosSubscriber):

    '''
    Connection with ROS regarding the incoming 3D Lidar data
    '''
    def __init__(self):
        super().__init__()
        try:
            self.sub_number = self.subscribe_to_topic(
                topic='/pcl_scan',
                message_type='sensor_msgs/PointCloud2',
                callback_function=self.receive_lidar3D_reading
            )
        except Exception:
            logger.error("Error while subscribing to 3D Lidar topic")
            raise

    def receive_lidar3D_reading(self, lidarData):
        if connector.RosConnector.is_connected():
            dataByte = bytes(lidarData['data'], 'utf8')
            lidar = Lidar3D(height=lidarData['height'], width=lidarData['width'], fields=lidarData['fields'],
                            is_bigendian=lidarData['is_bigendian'], point_step=lidarData['point_step'],
                            row_step=lidarData['row_step'], data=dataByte, is_dense=lidarData['is_dense'])
            lidar.save()